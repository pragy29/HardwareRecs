import re
from preprocessData_31940757 import preprocessLine


class Parser:
    """
	A class used to represent a Parser
    Attributes
    ----------
    inputString : str
        a string to store the post
    ID : int
        integer to store the row id of the post
    type : str
        string to store the post type
    dateQuarter : str
    	 a string to store the quarter and year of the post
	cleanBody : str
		a string to store the clean body of the post
    Methods
    -------
    __str__()
    	returns the string with the object attributes
    getID()
    	returns the postid
    getPostType()
        Returns the type of the post
    getDateQuarter()
    	returns the quarter and the year when the post was created
    getCleanedBody()
    	returns the clean body of the post
    getVocabularySize()
    	returns the unique word count

    """

    def __init__(self, inputString):
        self.inputString = inputString
        self.ID = self.getID()
        self.type = self.getPostType()
        self.dateQuarter = self.getDateQuarter()
        self.cleanBody = self.getCleanedBody()

    def __str__(self):
        # print ID, Question/Answer/Others, creation date, the main content
        print(str(self.ID), str(self.type), str(self.dateQuarter), str(self.cleanBody))

    def getID(self):
        post_id_list = re.findall('(?<=row Id=\")(.*)(?=\" PostTypeId)', self.inputString)
        post_id = int(post_id_list[0])
        return post_id

    def getPostType(self):
        post_type_list = re.findall('(?<=PostTypeId=\")(.*)(?=\" CreationDate)', self.inputString)
        post_type_id = int(post_type_list[0])
        post_type = ''
        if post_type_id == 1:
            post_type = 'question'
        elif post_type_id == 2:
            post_type = 'answer'
        else:
            post_type = 'other'
        return post_type

    # except:
    # 	post_type = ''
    # 	print("Some error occured.")
    # 	return post_type

    def getDateQuarter(self):
        try:
            date_list = re.findall('(?<=CreationDate=\")(.*)(?=\" Body)', self.inputString)
            creation_date = date_list[0]
            quarter = ""
            if int(creation_date[5:7]) in (1, 2, 3):
                quarter = str(creation_date[0:4]) + "Q1"
            elif int(creation_date[5:7]) in (4, 5, 6):
                quarter = str(creation_date[0:4]) + "Q2"
            elif int(creation_date[5:7]) in (7, 8, 9):
                quarter = str(creation_date[0:4]) + "Q3"
            elif int(creation_date[5:7]) in (10, 11, 12):
                quarter = str(creation_date[0:4]) + "Q4"
            return quarter
        except:
            quarter = ""
            print('Some error occured!')
            return quarter

    def getCleanedBody(self):
        clean_data_dict = preprocessLine(self.inputString)
        clean_data = clean_data_dict[1][1]
        return clean_data

    def getVocabularySize(self):
        try:
            content_body = re.sub('[^\w\s]', '', self.cleanBody.lower())
            content_body_list = content_body.split(" ")
            content_body_set = set(content_body_list)
            if "" in content_body_set:
                content_body_set.remove("")
            word_count = len(content_body_set)
            return word_count
        except:
            print("Some error occured!")
            return 0


#
# with open('data.xml', 'r') as file:
# 	file_content = file.readlines()
# 	print(file_content)
parser_obj = Parser(
    '<row Id="9321" PostTypeId="2" CreationDate="2018-06-06T18:10:55.257" Body="&lt;p&gt;I can\'t really say how effective it will be in an open space, but since your goal is to obfuscate the noise coming from your conversation, your options are pretty much limited to:&lt;/p&gt;&#xA;&#xA;&lt;ul&gt;&#xA;&lt;li&gt;containing your sound&lt;/li&gt;&#xA;&lt;li&gt;generating additional unrelated sound&lt;/li&gt;&#xA;&lt;/ul&gt;&#xA;&#xA;&lt;p&gt;Many psychiatrist\'s offices use &lt;a href=&quot;https://rads.stackoverflow.com/amzn/click/B00HD0ELFK&quot; rel=&quot;nofollow noreferrer&quot;&gt;devices like these&lt;/a&gt; outside the closed office door to act as a sonic barrier between noise in the room and noise in the hallway. It is a fairly low-tech solution as it is essentially a small, very noisy fan within an acoustic amplification chamber. It is adjustable somewhere between &quot;medium&quot; and &quot;loud&quot;. Its effectiveness will depend on how loud you are being and how close you are to the door.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Source: my wife and I use this specific model to provide white noise when we sleep.&lt;/p&gt;&#xA;" />')
print(parser_obj.getVocabularySize())
print(parser_obj.cleanBody)
