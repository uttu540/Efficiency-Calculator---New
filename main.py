from os import name
import numpy as np
from flask import Flask, request, jsonify, render_template
import urllib.request
from math import cos, expm1
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import csv
import sys

app = Flask(__name__)

@app.route('/')
def landingPage():
    return render_template('Efficiency_Calculator.html')

@app.route('/post', methods=['POST'])

def post():
    questionWeight, maxAnswerScore = 4, 4
    maxASMultipleChoice = 10
    answerScore, answerScore2,answerScore3, answerScore4, answerScore5, answerScore6, answerScore7, answerScore8, answerScore9, answerScore10, answerScore11, answerScore12, answerScore13, answerScore14, answerScore15, answerScore16,answerScore17, answerScore18, answerScore19, answerScore20, answerScore21, answerScore22, answerScore23, answerScore24, answerScore25  = ([] for _ in range(25))
    sectionWeight1 = 16
    sectionWeight2 = 24
    sectionWeight3 = 12
    sectionWeight4 = 16
    sectionWeight5 = 16
    sectionWeight6 = 16
    questionScore, questionScore2, questionScore3, questionScore4, questionScore5, questionScore6, questionScore7, questionScore8, questionScore9, questionScore10, questionScore11, questionScore12, questionScore13, questionScore14, questionScore15, questionScore16, questionScore17, questionScore19, questionScore20, questionScore21, questionScore22, questionScore23, questionScore24, questionScore25 =  (0 for _ in range(25))
    if request.method == "POST":
        participationOfTrainee = request.form.get('q49_waysTo49')

        if participationOfTrainee == 'Daily Attendance':
            answerScore.append(1)
        
        elif participationOfTrainee == 'Daily attendance and asking questions to check students&#x27; attentiveness':
            answerScore.append(2)
        
        elif participationOfTrainee == 'Using digital tools (e.g., Kahoot, Poll Everywhere) to take polls, quizzes to check attentiveness and then mark attendance':
            answerScore.append(3)

        elif participationOfTrainee == 'Digital tools to check daily attendance with various integrations to provide daily analytics':
            answerScore.append(4)

        questionScore = sum(answerScore)/ maxAnswerScore
        weightedQuestionScore = questionScore * questionWeight

        stakeholderCommunication  = request.form.get('q50_howDo50')

        if stakeholderCommunication == 'In-person conversations, such as one-to-one meetings, group discussions, classes etc.':
            answerScore2.append(1)
        
        elif stakeholderCommunication == 'Email':
            answerScore2.append(2)
        
        elif stakeholderCommunication == 'Email and meetings':
            answerScore2.append(3)

        elif stakeholderCommunication == 'Through an LMS or LXP':
            answerScore2.append(4)

        questionScore2 = sum(answerScore2)/ maxAnswerScore
        weightedQuestionScore2 = questionScore2 * questionWeight


        bigChallenges  = request.form.get('q51_whatIs')

        if bigChallenges == 'There are too many platforms for different tasks':
            answerScore3.append(1)
        
        elif bigChallenges == 'Managing course delivery seamlessly':
            answerScore3.append(2)
        
        elif bigChallenges == 'Managing tests and quizzes':
            answerScore3.append(3)

        elif bigChallenges == 'Managing and analyzing feedback':
            answerScore3.append(4)

        questionScore3 = sum(answerScore3)/ maxAnswerScore
        weightedQuestionScore3 = questionScore3 * questionWeight

        historicalData  = request.form.get('q64_whereDo')

        if historicalData == 'I don&#x27;t keep record of such data':
            answerScore4.append(1)
        
        elif historicalData == 'Log Book':
            answerScore4.append(2)
        
        elif historicalData == 'Multiple platform for different types of historical data':
            answerScore4.append(3)

        elif historicalData == 'An online platform where all types of historical data is collected centrally and stored':
            answerScore4.append(4)

        questionScore4 = sum(answerScore4)/ maxAnswerScore
        weightedQuestionScore4 = questionScore4 * questionWeight


        sectionScore = sectionWeight1 * (weightedQuestionScore + weightedQuestionScore2 + weightedQuestionScore3 + weightedQuestionScore4)

        #Section 2 

        typeFeedback = request.form.get('q46_whatType')

        if typeFeedback == 'I don&#x27;t collect feedback from my attendees':
            answerScore5.append(1)
        
        elif typeFeedback == 'Post Training Survey':
            answerScore5.append(2)
        
        elif typeFeedback == 'Daily feedback using polls and surveys':
            answerScore5.append(3)

        elif typeFeedback == 'Pre-Assessment to assess expectations and Post-Training surveys':
            answerScore5.append(4)

        questionScore5 = sum(answerScore5)/ maxAnswerScore
        weightedQuestionScore5 = questionScore5 * questionWeight


        surveyCreation  = request.form.get('q20_howDo')

        if surveyCreation == 'Through hardcopy surveys handed out in the training event':
            answerScore6.append(1)
        
        elif surveyCreation == 'Through standard, online forms':
            answerScore6.append(2)
        
        elif surveyCreation == 'Through personalized, online forms':
            answerScore6.append(3)

        elif surveyCreation == 'Through personalized, online forms using science-backed templates':
            answerScore6.append(4)

        questionScore6 = sum(answerScore6)/ maxAnswerScore
        weightedQuestionScore6 = questionScore6 * questionWeight


        feedbackTools  = request.form.get('q61_whatTools')

        if feedbackTools == 'I don&#x27;t use tools to collect feedback (verbal or written feedback)':
            answerScore7.append(1)
        
        elif feedbackTools == 'Through hard-copy surveys handed out in the training event':
            answerScore7.append(2)
        
        elif feedbackTools == 'I collect feedback with standard survey tools like Google Forms, Survey Monkey, etc.':
            answerScore7.append(3)

        elif feedbackTools == 'I collect feedback with a tool that is integrated in a platform I use':
            answerScore7.append(4)

        questionScore7 = sum(answerScore7)/ maxAnswerScore
        weightedQuestionScore7 = questionScore7 * questionWeight


        realTimeAnalysis  = request.form.get('q19_howDo')

        if realTimeAnalysis == 'I analyze data manually from hard-copy feedback I received from attendees':
            answerScore8.append(1)
        
        elif realTimeAnalysis == 'I analyze data with a digital spreadsheet (Excel, Google Sheets, etc)':
            answerScore8.append(2)
        
        elif realTimeAnalysis == 'I rely on a team/team member that analyzes the data and provides analytics with BI Tools (i.e. PowerBI, Tableau, etc)':
            answerScore8.append(3)

        elif realTimeAnalysis == 'I have an LMS or LXP that analyzes feedback and provides recommendations or suggestions.':
            answerScore8.append(4)

        questionScore8 = sum(answerScore8)/ maxAnswerScore
        weightedQuestionScore8 = questionScore8 * questionWeight

        frequecyOfFeedback  = request.form.get('q55_howFrequently')

        if frequecyOfFeedback == 'Each quarter':
            answerScore9.append(1)
        
        elif frequecyOfFeedback == 'Every 6 months':
            answerScore9.append(2)
        
        elif frequecyOfFeedback == 'At the end of each course':
            answerScore9.append(3)

        elif frequecyOfFeedback == 'I have real-time data that i can always consult':
            answerScore9.append(4)

        questionScore9 = sum(answerScore9)/ maxAnswerScore
        weightedQuestionScore9 = questionScore9 * questionWeight

        midCourseFeedback  = request.form.get('q66_doYou66')

        if midCourseFeedback == 'Yes':
            answerScore10.append(0)
        
        elif midCourseFeedback == 'No':
            answerScore10.append(4)

        questionScore10 = sum(answerScore10)/ maxAnswerScore
        weightedQuestionScore10 = questionScore10 * questionWeight


        sectionScore2 = sectionWeight2 * (weightedQuestionScore5 + weightedQuestionScore6 + weightedQuestionScore7 + weightedQuestionScore8 + weightedQuestionScore9 + weightedQuestionScore10)

        #Section 3 
        # New Way of doing and Evaluating Training

        differentWaysEvaluatingTraining = request.form.get('q65_whatAre')

        if differentWaysEvaluatingTraining == 'Analyze the performance of the employee manually without any parameters':
            answerScore11.append(1)
        
        elif differentWaysEvaluatingTraining == 'ROI calculator':
            answerScore11.append(2)
        
        elif differentWaysEvaluatingTraining == 'ROI calculator and through feedback received from the employees':
            answerScore11.append(3)

        elif differentWaysEvaluatingTraining == 'Using training evaluation platform or an efficiency calculator':
            answerScore11.append(4)

        questionScore11 = sum(answerScore11)/ maxAnswerScore
        weightedQuestionScore11 = questionScore11 * questionWeight

        toolsEaseTraining  = request.form.get('q26_whatTools26')

        if toolsEaseTraining == 'Individualized Learning':
            answerScore12.append(1)
        
        elif toolsEaseTraining == 'Accessible Content':
            answerScore12.append(2)
        
        elif toolsEaseTraining == 'Recording of sessions':
            answerScore12.append(3)

        elif toolsEaseTraining == 'All of the above':
            answerScore12.append(4)

        questionScore12 = sum(answerScore12)/ maxAnswerScore
        weightedQuestionScore12 = questionScore12 * questionWeight


        toolsProvidedTrainers  = request.form.get('q47_whatTools47')

        if toolsProvidedTrainers == 'Cloud Presentations':
            answerScore13.append(1)
        
        elif toolsProvidedTrainers == 'Engagement Tools (Polling tools, google classroom, slack)':
            answerScore13.append(2)
        
        elif toolsProvidedTrainers == 'Interactive Dashboards':
            answerScore13.append(3)

        elif toolsProvidedTrainers == 'All of the above':
            answerScore13.append(4)

        questionScore13 = sum(answerScore13)/ maxAnswerScore
        weightedQuestionScore13 = questionScore13 * questionWeight


        sectionScore3 = sectionWeight3 * (weightedQuestionScore11 + weightedQuestionScore12 + weightedQuestionScore13)

        # Section 4

        # Real-time Communication and Collaboration Systems

        meaniningfulCommunication  = request.form.get('q62_whatAre62')

        if meaniningfulCommunication == 'Classroom debates':
            answerScore14.append(1)
        
        elif meaniningfulCommunication == 'Discussions offline or online':
            answerScore14.append(2)
        
        elif meaniningfulCommunication == 'Presentation with Q+A':
            answerScore14.append(3)

        elif meaniningfulCommunication == 'A platform with multiple opportunities for effective communication (discussion forum, video conferencing tools, etc)':
            answerScore14.append(4)

        questionScore14 = sum(answerScore14)/ maxAnswerScore
        weightedQuestionScore14 = questionScore14 * questionWeight


        collaborativeTraining  = request.form.get('q63_howDo63')

        if collaborativeTraining == 'Offline discussion':
            answerScore15.append(1)
        
        if collaborativeTraining == 'Discussion Forums':
            answerScore15.append(2)
        
        if collaborativeTraining == 'Digital Tools like Slack, Miro, etc.':
            answerScore15.append(3)

        if collaborativeTraining == 'A platform where I utilize digital tools and create discussion forums':
            answerScore15.append(4)

        questionScore15 = sum(answerScore15)/ maxAnswerScore
        weightedQuestionScore15 = questionScore15 * questionWeight

        shareInformation = request.form.get('q63_howDo63')

        if shareInformation == 'Inform everyone using a flier placed on a bulletin board':
            answerScore16.append(1)
        
        if shareInformation == 'Share information with organization leaders, who will pass-down the information':
            answerScore16.append(2)
        
        if shareInformation == 'Using communication apps like WhatsApp, Slack,etc.':
            answerScore16.append(3)

        if shareInformation == 'A training platform with notifications, emails, and messaging built into the platform':
            answerScore16.append(4)

        questionScore16 = sum(answerScore16)/ maxAnswerScore
        weightedQuestionScore16 = questionScore16 * questionWeight

        collaborateDifferentEntities  = request.form.get('q58_typeA')

        if collaborateDifferentEntities == 'Offline group discussion and team building activities':
            answerScore17.append(1)
        
        if collaborateDifferentEntities == 'Group meetings and brainstorming within the group':
            answerScore17.append(2)
        
        if collaborateDifferentEntities == 'Encouraging participation and allowing everyone to share their perspective':
            answerScore17.append(3)

        if collaborateDifferentEntities == 'An online platform which provides group discussion boards, meetings, brainstorming softwares etc':
            answerScore17.append(4)

        questionScore17 = sum(answerScore17)/ maxAnswerScore
        weightedQuestionScore17 = questionScore17 * questionWeight


        sectionScore4 = sectionWeight4 * (weightedQuestionScore14 + weightedQuestionScore15 + weightedQuestionScore16 + weightedQuestionScore17)


        # Section 5

        # Build Relationship and Growth

        buildCommunity  = request.form.get('q48_doYou48')

        if buildCommunity == 'Yes':
            answerScore18.append(4)
        
        elif buildCommunity == 'No':
            answerScore18.append(0)
        

        questionScore18 = sum(answerScore18)/ maxAnswerScore
        weightedQuestionScore18 = questionScore18 * questionWeight


        alumniEvents = request.form.get('q59_howOften')

        if alumniEvents == 'I don&#x27;t conduct alumni events':
            answerScore19.append(1)
        
        elif alumniEvents == 'Every 3 months':
            answerScore19.append(4)
        
        elif alumniEvents == 'Every 6-9 months':
            answerScore19.append(3)

        elif alumniEvents == 'Once a year':
            answerScore19.append(2)

        questionScore19 = sum(answerScore19)/ maxAnswerScore
        weightedQuestionScore19 = questionScore19 * questionWeight
        
        
        marketingPromotion  = request.form.get('q60_howDo60')

        if marketingPromotion == 'Word of mouth':
            answerScore20.append(1)
        
        elif marketingPromotion == 'Webinars':
            answerScore20.append(2)
        
        elif marketingPromotion == 'Emails':
            answerScore20.append(3)

        elif marketingPromotion == 'Marketing campaigns on social media platforms':
            answerScore20.append(4)

        questionScore20 = sum(answerScore20)/ maxAnswerScore
        weightedQuestionScore20 = questionScore20 * questionWeight

        checkOnEmployees  = request.form.get('q67_howDo67')

        if checkOnEmployees == 'I don&#x27;t check and notify the employee':
            answerScore21.append(1)
        
        elif checkOnEmployees == 'Notify the employee through email':
            answerScore21.append(2)
        
        elif checkOnEmployees == 'One-to-one discussion':
            answerScore21.append(3)

        elif checkOnEmployees == 'Notify the employee through the platform the organization is using to provide training and encouraging the employee through one-to-one meeting':
            answerScore21.append(4)

        questionScore21 = sum(answerScore21)/ maxASMultipleChoice
        weightedQuestionScore21 = questionScore21 * questionWeight


        sectionScore5 = sectionWeight5 * (weightedQuestionScore18 + weightedQuestionScore19 + weightedQuestionScore20 + weightedQuestionScore21)

        #Section 6

        # Transparency and Access of Content

        provideDetails  = request.form.get('q39_doYou')

        if provideDetails == 'Yes':
            answerScore22.append(4)
        
        elif provideDetails == 'No':
            answerScore22.append(0)
        

        questionScore22 = sum(answerScore22)/ maxAnswerScore
        weightedQuestionScore22 = questionScore22 * questionWeight


        provideRubrics  = request.form.get('q40_doYou40')

        if provideRubrics == 'Yes':
            answerScore23.append(4)
        
        elif provideRubrics == 'No':
            answerScore23.append(0)

        questionScore23 = sum(answerScore23)/ maxAnswerScore
        weightedQuestionScore23 = questionScore23 * questionWeight

        informationToTrainers  = request.form.get('q43_name43[]')

        if informationToTrainers == 'Trainee Information':
            answerScore24.append(1)
        
        elif informationToTrainers == 'Course materials (presentations, syllabus, etc.)':
            answerScore24.append(2)
        
        elif informationToTrainers == 'A list of courses to help the trainers revise for better course delivery':
            answerScore24.append(3)

        questionScore24 = sum(answerScore24)/ maxASMultipleChoice
        weightedQuestionScore24 = questionScore24 * questionWeight


        informationToTrainees = request.form.get('q44_name44[]')

        if informationToTrainees == 'Course prerequisites':
            answerScore25.append(1)
        
        elif informationToTrainees == 'Syllabus':
            answerScore25.append(2)
        
        elif informationToTrainees == 'Trainer&#x27;s Details':
            answerScore25.append(3)

        elif informationToTrainees == 'Course objectives':
            answerScore25.append(4)

        questionScore25 = sum(answerScore25)/ maxASMultipleChoice
        weightedQuestionScore25 = questionScore25 * questionWeight


        sectionScore6 = sectionWeight6 * (weightedQuestionScore22 + weightedQuestionScore23 + weightedQuestionScore24 + weightedQuestionScore25)



        totalScore = sectionScore + sectionScore2 + sectionScore3 + sectionScore4 + sectionScore5 + sectionScore6
        maxScore = sectionWeight1 + sectionWeight2 + sectionWeight3 + sectionWeight4 + sectionWeight5 + sectionWeight6
        totalScore10 = totalScore/10
    return render_template("resultReport.html", value = round(totalScore10), section1 = round(sectionScore/5), section2 = round(sectionScore2/5), section3 = round(sectionScore3/5), section4 = round(sectionScore4/5), section5 = round(sectionScore5/5), section6 = round(sectionScore6/5))


if __name__=='__main__':
   app.run(debug=True, port=5001)