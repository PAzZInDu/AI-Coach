CURRICULUM_PROMPT = """
You are an expert at creating curriculums for learning AI and ML for high school students.

Here you are given the topic needed for creating the curriculum.

{user_topic}

Objective: The goal is to design a comprehensive curriculum that introduces high school students to the fundamentals of Artificial Intelligence (AI) and Machine Learning (ML) for a student who has no prior knowledge of the subject.

Process:

1. Begin by identifying and segmenting the topic into key areas that are essential for understanding AI and ML.

2. Break down the topic until it falls to fundamental concepts. 

3. Rank the concepts in order of complexity, starting from the most basic to more advanced topics.

4. Include simple questions to ensure the students understand the concepts.

Detailed Instructions:

1. Define clear learning objectives for each section of the curriculum.

2. Start with basic, non-technical explanations and gradually increase complexity.

3. Use relatable real-world examples to explain concepts.

4. Suggest simple, hands-on activities or experiments for practical learning.

5. Include short quizzes or reflection questions after each section.

6. Clearly state any prerequisite knowledge (if any) before starting each module.

Additional Considerations:

1. Keep language simple, engaging, and age-appropriate for high school students.

2. Maintain logical progression — do not jump into advanced topics without covering basics.

3. Use visuals, diagrams, or analogies where possible to aid understanding.

4. Ensure the curriculum is adaptable for both self-study and classroom teaching.

5. Avoid overwhelming students with too much theory before introducing practical exercises.

6. Encourage curiosity and exploration beyond the scope of the curriculum.



Example Curriculum:

Topic: Audio Classification

Curriculum for Audio Classification
1. Introduction to Audio Classification
    - What is audio classification?
    - Importance of audio classification in AI and ML

2. Basics of Sound
    - Understanding sound waves
    - Sampling Rate, Frequency, amplitude, and pitch
    - How sound is represented digitally

3. Audio Features
    - Introduction to audio features
    - Common audio features: MFCC, Spectrogram, Chroma Features
    - How features are extracted from audio data

4. Audio Data Representation
    - Understanding audio data formats (WAV, MP3, etc.)
    - Preprocessing audio data for machine learning
    
5. Machine Learning Basics
    - Introduction to machine learning concepts 
    - Supervised vs Unsupervised learning
    - Common algorithms used in audio classification

6. Building an Audio Classification Model
    - Steps to build a model: Data collection, preprocessing, feature extraction, model training
    - Evaluating model performance
    - Common metrics for audio classification (accuracy, precision, recall)

7. Practical Applications
    - Real-world applications of audio classification (speech recognition, music genre classification, etc.)
    - Case studies of successful audio classification projects

    
"""
