import re
def preprocessLine(inputLine):
    """
    This method takes in one input parameter and performs the task of data cleaning on the input line .
    @param inputLine: This input parameter is going to be a part of xml tag from which meaningful data is to be
     extracted
    @return processed_dict: The method returns a dictionary containing the post type id and the clean body content
    """
    # preprocess the data in each line

    try:
        content_dict = {}
        processed_dict = {}
        dict_key = 1
        # conditional operator to check whether the xml tag contain PostTypeId i.e. relevant xml tags for our use
        if re.search('(?<=PostTypeId=\")(.*)(?=\" CreationDate)', inputLine):
            # finds all the lines containing posttypeid for us ot extract its values
            post_type = re.findall('(?<=PostTypeId=\")(.*)(?=\" CreationDate)', inputLine)
            # finds all the lines containing Body for us ot extract its values
            reg_content_list = re.findall('(?<=Body=\")(.*)(?=;\")', inputLine)
            if reg_content_list and post_type:
                # stores the contents in a dictionary
                for i in reg_content_list:
                    content_dict[dict_key] = [post_type[0], i]
                dict_key += 1
            else:
                content_dict[dict_key] = [post_type[0], ""]
            for key in content_dict:
                processed_str = ""
                split_content = content_dict[key][1].split(';')
                # removes the xml tags and replaces it with the html tags from the body
                for lines in split_content:
                    lines = re.sub("&gt", '>', lines)
                    lines = re.sub("&amp", '&', lines)
                    lines = re.sub("&lt", '<', lines)
                    lines = re.sub("&#xA", '', lines)
                    lines = re.sub("&#xD", '', lines)
                    lines = re.sub('href=', '', lines)
                    lines = re.sub('&quot', '\'', lines)
                    processed_str += lines
                    processed_dict[key] = [content_dict[key][0], processed_str]
            for key in processed_dict.keys():
                # removes all the html tags from the body and stores in a new dictionary
                for content in processed_dict:
                    processed_dict[content][1] = re.sub('<[^>]*>', "", processed_dict[content][1])
        return processed_dict
    except:
        processed_dict = {}
        return processed_dict


def splitFile(inputFile, outputFile_question, outputFile_answer):
    """
    This function will recieve three input files as parameters. It will perform data cleaning on inputFile and
    split the data into question and answers based on the posttypeid and store the data into relevant question
    or answer file.
    @param inputFile: File containing xml data
    @param outputFile_question: file to be written with the questions in the post xml file
    @param outputFile_answer: file to be written with the answers in the post xml file
    @return: Boolean depending on succes or failure of the function
    """
    # preprocess the original file, and split them into two files.
    try:
        q_no = 1
        a_no = 1
        # opens the input file in read mode
        with open(inputFile, 'r', encoding='utf-8') as file:
            # opens the question file in write mode
            with open(outputFile_question, 'w') as q_file:
                # open the answer file in write mode
                with open(outputFile_answer, 'w') as a_file:
                    file_content = file.readlines()
                    # loops through the input data and calls the above method to get a clean body content
                    for content in file_content:
                        preprocess_data = preprocessLine(content)
                        if preprocess_data:
                            for keys in preprocess_data:
                                if int(preprocess_data[keys][0]) == 1:
                                    # writes data into question file
                                    q_file.write(str(q_no) + ": " + preprocess_data[keys][1] + '\n')
                                    q_no += 1
                                elif int(preprocess_data[keys][0]) == 2:
                                    # writes data into answer file
                                    a_file.write(str(a_no) + ": " + preprocess_data[keys][1] + '\n')
                                    a_no += 1
        return True
    except FileNotFoundError as e:
        print("Sorry no file was found")
        return False
    except:
        return False


# if __name__ == "__main__":
#     f_data = "data.xml"
#     f_question = "question.txt"
#     f_answer = "answer.txt"
#
# splitFile(f_data, f_question, f_answer)
