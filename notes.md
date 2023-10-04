# Notes 


__INSTALL RUST COMPILER__

## Command-line usage

The following command will transcribe speech in audio files, using the medium model:

whisper audio.flac audio.mp3 audio.wav --model medium

The default setting (which selects the small model) works well for transcribing English. To transcribe an audio file containing non-English speech, you can specify the language using the --language option:

whisper japanese.wav --language Japanese

Adding --task translate will translate the speech into English:

whisper japanese.wav --language Japanese --task translate

Run the following to view all available options:

whisper --help
