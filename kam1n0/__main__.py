import sys
import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.StreamHandler()
    ])

if __name__ == "__main__":
    from kam1n0.processor import process_folder
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dir', nargs='?', help='The folder that contians binaries.')
    parser.add_argument('model', nargs='?', default='asmbin2vec', choices=[
                        'asmclone', 'asm2vec', 'asmbin2vec', 'sym1n0'],
                        help='The model to be used.')

    args = parser.parse_args()
    process_folder(args.dir, model=args.model, show_stdout=True)
