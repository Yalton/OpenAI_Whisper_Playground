import whisper
import argparse

def getArgs(): 

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--model', '-m', type=str, required=True)
    parser.add_argument('--audio', '-a', type=str, required=True)
    parser.add_argument("--filewrite", '-f', action="store_true")
    parser.add_argument('--filename', '-fn', type=str)
    return parser.parse_args()


def main(): 
    args = getArgs()
    model = whisper.load_model(args.model)
    result = model.transcribe(args.audio)


    if (args.filewrite):
        file = open(args.filename, "w")
        file.write(result["text"])
        file.close()

    else: 
        print(result["text"])


if __name__ == '__main__':
    main()