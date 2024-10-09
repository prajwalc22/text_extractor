import datetime
import whisper

model = whisper.load_model('base.en')

option = whisper.DecodingOptions(language='en',fp16 = False )

result = model.transcribe(' ') #give path to file in quotes

save_target = 'file_name.txt'

with open(save_target,'w') as file:
    for indx, segment in enumerate(result['segments']):
        file.write(str(indx + 1) + '\n')
        file.write(str(datetime.timedelta(seconds=segment['start'])) + '-->' + str(datetime.timedelta(seconds=segment['end'])) + '\n' )
        file.write(segment['text'].strip() + '\n')
        file.write('\n')


        


result ['segments'][0]
