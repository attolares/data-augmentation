from pdf2image import convert_from_path, convert_from_bytes

file = 'saidaDataset3times12'
convert_from_path(file+'.pdf', dpi=300, output_folder='75dpi/'+file, fmt='jpg')


