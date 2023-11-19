from audiocraft.models import musicgen
import time
import uuid
import logging
import os
import io
from audiocraft.data.audio import audio_write

# Set logging level to INFO
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():

    logger.info('Loading model...')
    model = musicgen.MusicGen.get_pretrained('large', device='cuda')
    duration = int(os.environ.get('DURATION', 8))
    logger.info(f"Duration: {duration} seconds")
    model.set_generation_params(duration=duration)

    # Read list of prompts from txt file
    with open('prompts.txt', 'r') as f:
        prompts = f.read().splitlines()

    # Log prompts
    logger.info('Prompts:')
    for prompt in prompts:
        logger.info(f'Prompt: {prompt}')

    # Generate from prompts
    logger.info('Generating audio...')
    start_time = time.time()
    wav = model.generate(prompts)
    end_time = time.time()

    logger.info(f'Audio generated in {end_time - start_time} seconds')

    for idx, one_wav in enumerate(wav):
        # Generate a random name for file
        filename = prompts[idx].replace(' ', '_')
        filename += '_' + str(uuid.uuid4())
        # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
        audio_write(f'output/{filename}', one_wav.cpu(), model.sample_rate, strategy="loudness")
    

if __name__ == '__main__':
    main()
