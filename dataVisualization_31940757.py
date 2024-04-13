import pandas as pd
import matplotlib.pyplot as plt
from parser_31940757 import Parser
import re


def visualizeWordDistribution(inputFile, outputImage):
    """
    This method is used to create a bar plot of the word distribution trend
    @param inputFile: this is the xml file containing the post data
    @param outputImage: the ouput png file containing the plot
    @return: boolean indicating if thw method executed successfully or not
    """
    try:
        object_dict = {}
        frequency_dict = {'0-10': 0, '10-20': 0, '20-30': 0, '30-40': 0, '40-50': 0, '50-60': 0, '60-70': 0, '70-80': 0, '80-90': 0, '90-100': 0, 'others': 0}
        dict_key = 1
        with open(inputFile, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
            for content in file_content:
                if re.search('(?=<row Id)(.*)(?=/>)', content):
                    parser_obj = Parser(content)
                    word_count = parser_obj.getVocabularySize()
                    object_dict[parser_obj.ID] = word_count
        for keys in object_dict:
            if object_dict[keys] in range(0, 10):
                frequency_dict['0-10'] += 1
            elif object_dict[keys] in range(10, 20):
                frequency_dict['10-20'] += 1
            elif object_dict[keys] in range(20, 30):
                frequency_dict['20-30'] += 1
            elif object_dict[keys] in range(30, 40):
                frequency_dict['30-40'] += 1
            elif object_dict[keys] in range(40, 50):
                frequency_dict['40-50'] += 1
            elif object_dict[keys] in range(50, 60):
                frequency_dict['50-60'] += 1
            elif object_dict[keys] in range(60, 70):
                frequency_dict['60-70'] += 1
            elif object_dict[keys] in range(70, 80):
                frequency_dict['70-80'] += 1
            elif object_dict[keys] in range(80, 90):
                frequency_dict['80-90'] += 1
            elif object_dict[keys] in range(90, 100):
                frequency_dict['90-100'] += 1
            else:
                frequency_dict['others'] += 1

        df = pd.DataFrame(frequency_dict.items())
        df_final = df.rename(columns={0: "SizeRange", 1: "Frequency"})
        print(df_final)

        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(df_final.SizeRange, df_final.Frequency, color='maroon',
                width=0.4)

        plt.xlabel("Vocab Size Range")
        plt.ylabel("No. of Posts")
        plt.title("Distribution of Vocab Size Across Posts")

        plt.savefig(outputImage)
        return True

    except FileNotFoundError as e:
        object_dict = {}
        print("Sorry file not found")
        return False
    except Exception as e:
        object_dict = {}
        print(e)
        return False


def visualizePostNumberTrend(inputFile, outputImage):
    """
    This method is used to analyze the trend for question and answers posted to over the years and quarters
    @param inputFile: this is the xml file containing the post data
    @param outputImage: the ouput png file containing the plot
    @return: boolean indicating if thw method executed successfully or not
    """
    try:
        ques = {}
        ans = {}
        with open(inputFile, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
            for content in file_content:
                if re.search('(?=<row Id)(.*)(?=/>)', content):
                    parser_obj = Parser(content)
                    if parser_obj.getPostType().lower() == 'question':
                        ques[parser_obj.getID()] = parser_obj.getDateQuarter()
                    elif parser_obj.getPostType().lower() == 'answer':
                        ans[parser_obj.getID()] = parser_obj.getDateQuarter()

            ques_df = pd.DataFrame(ques.items(), columns=['post_id', 'date_quarter'])
            ques_df = ques_df.groupby('date_quarter')['post_id'].count().reset_index()

            ans_df = pd.DataFrame(ans.items(), columns=['post_id', 'date_quarter'])
            ans_df = ans_df.groupby('date_quarter')['post_id'].count().reset_index()

            x = ans_df['date_quarter']
            y1 = ques_df['post_id']
            y2 = ans_df['post_id']

            fig = plt.figure(figsize=(20, 10))

            plt.title("Questions and Answers Trends - Quarterly")
            plt.plot(x, y1, label="Questions")
            plt.plot(x, y2, label="Answers")
            plt.legend()
            plt.savefig(outputImage)
            return True
    except:
        print("Some error occurred.")
        return False


if __name__ == "__main__":
    f_data = "data.xml"
    f_wordDistribution = "vocabularySizeDistribution.png"
    f_postTrend = "postNumberTrend.png"

    visualizeWordDistribution(f_data, f_wordDistribution)
    visualizePostNumberTrend(f_data, f_postTrend)

# visualizePostNumberTrend(f_data, f_postTrend)
