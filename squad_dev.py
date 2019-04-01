import json
import os
with open('dev-v2.0.json') as json_file:

    data_p = json.load(json_file)
# Main directory
    output_dir="/Users/Prathusha/Desktop/squad_dev/venv/paragraphs"
# The data set has passages based on multiple topics so get the topic at each level
    for topic in data_p["data"]:

        title = topic["title"]
        path = os.path.join(output_dir,title)
        os.mkdir(path)
        print(title)
        i=0
# Every topic has varying number of passages so save each paragraph in a new .txt file
        for paragraph in topic["paragraphs"]:
            # print(paragraph["context"])
            output_path=os.path.join(output_dir,title,str(i))+"_"+title+".txt"
            # print(output_path)
            output_file = open(output_path,"w")
            output_file.write(paragraph["context"].encode("utf-8"))

            i += 1




