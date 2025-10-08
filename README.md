# Joana Azevedo Portfolio

**Master's in Digital Humanities at Minho University in Portugal** 

-------------

## Index:

1. [Project 1 - Text Processing and Analysis with Python](#Project-1---Text-Processing-and-Analysis-with-Python)
2. [Project 2 - Implementing Text Markup and Validation in XML and DTD](#Project-2---Implementing-Text-Markup-and-Validation-in-XML-and-DTD)
3. [Project 3 - Transcription and Modernization of Text into Functional HTML](#Project-3---Transcription-and-Modernization-of-Text-into-Functional-HTML)
4. [Project 4 - Exploring Syntax, Semantics, and Readability through Corpus Analysis](#Project-4---Exploring-Syntax,-Semantics,-and-Readability-through-Corpus-Analysis)
5. [Project 5 - Transcribing and Analyzing 18th-Century Manuscripts](#Project-5---Transcribing-and-Analyzing-18th-Century-Manuscripts)
6. [Project 6 - Corpus Construction and Linguistic Analysis of Family Interviews](#Project-6---Corpus-Construction-and-Linguistic-Analysis-of-Family-Interviews)
7. [Project 7 - Educational Mobile App Prototype Designed in Figma](#Project-7---Educational-Mobile-App-Prototype-Designed-in-Figma)
8. [Project 8 - Development of an Educational Game with Artificial Intelligence](#Project-8---Development-of-an-Educational-Game-with-Artificial-Intelligence)
9. [Project 9 - Web Design and Content Management for Conference Platforms with WordPress](#Project-9---Web-Design-and-Content-Management-for-Conference-Platforms-with-WordPress)
10. [Project 10 - Video Editing and Production of a Carpentry Lesson with DaVinci Resolve](#Project-10---Video-Editing-and-Production-of-a-Carpentry-Lesson-with-DaVinci-Resolve)
11. [Project 12 - Advanced Translation Tools Project](#Project-12---)
12. [Project 13 - Development of an Educational Mobile App Startup](#Project-13---Development-of-an-Educational-Mobile-App-Startup)

-------

## Project 1 - Text Processing and Analysis with Python

**Summary:**

This project was developed for the course Foundations and Natural Language Processing (FPLN).</br>
It focused on building a Python interface capable of reading, processing, and extracting information from textual files to explore language patterns and analyze website data.</br>
For this project, six recipes were selected from the 24 Kitchen website and saved as .txt files for detailed analysis.</br>
The project was carried out with guidance from Professor José João, who provided support with technical challenges and feedback on the overall approach.

**Main Objectives:**

- Consolidate knowledge from the Natural Language Processing course.
- Develop a Python program capable of processing multiple text files and extracting structured information.
- Implement textual analysis metrics, including word frequency, line count, sentence length, proper nouns, and shared vocabulary.
- Enable exporting of analyzed data in multiple formats (JSON, CSV, XML) for further use.

**Key Features and Tasks:**

- Extracted structured information from .txt files, including recipe title, author, ingredients, and preparation steps.
- Implemented web scraping from the 24 Kitchen website using *requests* and *BeautifulSoup*.
- Calculated word counts, line counts, frequency of user-selected words, top 10 most common words, proper nouns, and average sentence length.
- Identified common words across multiple texts, excluding simple stopwords and numbers.
- Built a terminal-based interactive interface allowing users to select files, run analyses, and export results.

**My Role and Contributions:**

- Developed Python scripts using *re*, *os*, *csv*, *json*, *xml.etree.ElementTree*, *requests*, *BeautifulSoup*, and *Counter*.
- Designed and implemented the main program flow and menu-driven interface for user interaction.
- Created functions for text extraction, analysis, and data export, ensuring modularity and reusability.
- Managed error handling for file access, web requests, and user inputs.

**Learnings and Outcomes:**

- Gained practical experience in Python programming for text processing and web scraping.
- Learned to apply natural language processing techniques to real-world textual data.
- Developed skills in organizing, structuring, and exporting data for further analysis.
- Experienced the benefits of automating text analysis, improving efficiency over manual methods.
- Enhanced understanding of project workflow, from data collection and processing to analysis and reporting.

---

## Project 2 - Implementing Text Markup and Validation in XML and DTD

**Summary:**

This project was developed for the course of Digital Editing and Analysis.</br>
The project focused on the digital modeling and markup of *Memorial de Varios Simplices* by João Curvo Semmedo, creating structured text documents using XML and defining validation rules with DTD.

**Main Objectives:**

- Understand markup languages and document structuring.
- Apply XML to encode textual data.
- Use DTD for validating document structures.

**Key Features and Tasks:**

- Defined a DTD (Document Type Definition) to structure elements of the work (titles, locus, geoName, citation, foreign, etc.).
- Created an XML document following TEI (Text Encoding Initiative) standards, ensuring compliance with the DTD.
- Inserted metadata in the <teiHeader> (author, title, date, source, and transcription responsibilities).
- Applied semantic markup to key elements such as <drug>, <ingredient>, and <herb> to enable future research and automated analysis.
- Included supporting images (<figure><graphic url="..."/></figure>) to visually contextualize excerpts.
- Structured sample texts in XML and ensured data consistency and proper formatting.

**My Role and Contributions:**

- Wrote XML files and corresponding DTDs.
- Marked up semantic elements to facilitate automated search and analysis.
- Tested validation rules to ensure compliance with schemas.

**Learnings and Outcomes:**

- Learned the principles of document markup, semantic tagging, and validation.
- Understood how structured data and TEI standards enhance readability, research potential, and consistency of historical texts.

---

## Project 3 - Transcription and Modernization of Text into Functional HTML

**Summary:**

This project was developed for the course Digital Editing and Analysis.</br>
It focused on the manual transcription and modernization of a historical text, transforming it into a fully functional, semantically structured HTML document.</br>
It also involved normalizing spelling, refining formatting, and ensuring web-ready readability.

**Main Objectives:**

- Transcribe the original text accurately.
- Convert the text into HTML with proper tags and semantic structure.
- Normalize and modernize the text for readability and usability on the web.

**Key Features and Tasks:**

- Applied HTML structure including headings, paragraphs, lists, and links where appropriate.
- Corrected spelling and modernized outdated expressions.
- Ensured the HTML code is clean, functional, and visually coherent.

**My Role and Contributions:**

- Transcribed the original text from source material.
- Marked up the text in HTML, adding semantic tags.
- Reviewed and modernized the content for clarity and usability.

**Learnings and Outcomes:**

- Gained hands-on experience with HTML coding and web formatting.
- Learned to normalize historical texts while maintaining their meaning.
- Improved skills in preparing textual content for digital publication.

---

## Project 4 - Exploring Syntax, Semantics, and Readability through Corpus Analysis

**Summary:**

A corpus-based analysis of texts comparing syntactic, semantic, and readability features across different types of documents.

**Main Objectives:**

- Study linguistic differences in various corpora.
- Analyze readability metrics and syntactic patterns.
- Compare lexical diversity across texts.

**Key Features and Tasks:**

- Calculated sentence length, lexical diversity (TTR), and semantic similarity.
- Created visualizations including boxplots and scatterplots.
- Identified patterns in syntax, semantics, and readability.

**My Role and Contributions:**

- Processed text corpora using Python and Pandas.
- Generated metrics and visualized results with Matplotlib and Seaborn.

**Learnings and Outcomes:**

- Developed skills in corpus analysis and visualization.
- Learned to interpret syntactic and semantic patterns in texts.

---

## Project 5 - Transcribing and Analyzing 18th-Century Manuscripts

**Summary:**

Manual transcription and linguistic analysis of 18th-century Portuguese manuscripts to study orthographic and lexical variations.

**Main Objectives:**

- Transcribe handwritten manuscripts into text format.
- Clean and normalize texts for analysis.
- Analyze orthographic variation and lexical patterns.

**Key Features and Tasks:**

- Transcribed historical manuscripts from PNG images.
- Standardized spellings and identified word variants.
- Conducted lexical and orthographic analysis.

**My Role and Contributions:**

- Carefully transcribed and proofread manuscripts.
- Organized texts for computational analysis.
- Analyzed variation in spelling and vocabulary.

**Learnings and Outcomes:**

- Improved skills in paleography and historical linguistics.
- Learned to manage and analyze historical text corpora.
----

## Project 6 - Corpus Construction and Linguistic Analysis of Family Interviews

**Summary:**

Collection, transcription, cleaning, and linguistic analysis of interviews with family members.

**Main Objectives:**

- Create a corpus from oral family interviews.
- Analyze lexical, syntactic, and semantic features.
- Understand language use in familial contexts.

**Key Features and Tasks:**

- Transcribed and cleaned audio interviews.
- Analyzed lexical diversity, syntactic complexity, and semantic content.
- Compared linguistic patterns across interviewees.

**My Role and Contributions:**

- Conducted manual transcription of recorded interviews.
- Applied computational analysis using Python and relevant NLP tools.

**Learnings and Outcomes:**

- Learned corpus construction from oral data.
- Gained experience in multi-level linguistic analysis.

---

## Project 7 - Educational Mobile App Prototype Designed in Figma

**Summary:**

Interactive mobile application prototype inspired by *Memorial de Varios Simples*, combining education and gamification.</br>
This project showcases an interactive mobile application prototype developed in Figma, inspired by João Curvo Semmedo’s Memorial de Varios Simples.</br>
The concept merges historical and educational dimensions, offering users an immersive experience that bridges the study of medicinal plants and traditional remedies with contemporary interaction design.</br>
Through quizzes, mini-games, and exploratory features, the app promotes active learning and engagement, illustrating how digital design can reinterpret historical knowledge for modern audiences.

**Main Objectives:**

- Create a functional Figma prototype.
- Design interactive learning experiences about plants and remedies.
- Include quizzes and mini-games to engage users.

**Key Features and Tasks:**

- Developed navigable screens and user flows.
- Designed educational and gamified elements.
- Implemented exploratory features for active learning.

**My Role and Contributions:**

- Designed the complete prototype in Figma.
- Integrated historical content into interactive elements.

**Learnings and Outcomes:**

- Developed UX/UI design skills for educational applications.
- Learned to integrate historical content into engaging digital formats.

---

## Project 8 - Development of an Educational Game with Artificial Intelligence

**Summary:**

Creation of an AI-powered educational game to facilitate interactive learning.

**Main Objectives:**

- Develop a learning game using AI techniques.
- Make the game engaging and educational.
- Explore AI applications in gamified learning.

**Key Features and Tasks:**

- Implemented AI-powered interactions and feedback.
- Designed game mechanics for educational purposes.
- Tested gameplay for engagement and learning outcomes.

**My Role and Contributions:**

- Developed game logic and AI components.
- Integrated content and interactive elements.

**Learnings and Outcomes:**

- Gained experience with AI in educational contexts.
- Learned to combine game design and computational logic for learning.

---

## Project 9 - Web Design and Content Management for Conference Platforms with WordPress

**Summary:**

Development of three websites for academic conferences using WordPress, focusing on design and content management.

**Main Objectives:**

- Design responsive conference websites.
- Manage content and provide user-friendly navigation.
- Ensure accessibility and professional presentation.

**Key Features and Tasks:**

- Created layouts and templates in WordPress.
- Uploaded and structured conference content.
- Ensured mobile responsiveness and usability.

**My Role and Contributions:**

- Built and customized websites in WordPress.
- Implemented content management strategies for smooth operation.

**Learnings and Outcomes:**

- Developed web design and WordPress management skills.
- Learned to create functional and aesthetically appealing conference platforms.

---

## Project 10 - Video Editing and Production of a Carpentry Lesson with DaVinci Resolve

**Summary:**

This project was developed for an extracurricular course in Video Editing for Digital Environments.</br>
The work consisted of recording and editing footage from a carpentry lesson to create a cohesive educational video using DaVinci Resolve.

**Main Objectives:**

- Capture footage of a carpentry class.
- Edit videos to create a coherent, instructive final product.
- Apply video editing techniques learned in class.

**Key Features and Tasks:**

- Recorded multiple lesson clips.
- Edited footage into a short, engaging video.
- Applied transitions, text overlays, and audio adjustments.

**My Role and Contributions:**

- Filmed lesson sequences.
- Edited video in DaVinci Resolve, adding learning highlights.

**Learnings and Outcomes:**

- Improved video production and editing skills.
- Learned to create clear, instructive multimedia content.

---

## Project 11 - 

**Summary:**

**Main Objectives:**

**Key Features and Tasks:**

**My Role and Contributions:**

**Learnings and Outcomes:**

---

### Project 12 - Development of an Educational Mobile App Startup

**Summary:**

**Main Objectives:**

**Key Features and Tasks:**

**My Role and Contributions:**

**Learnings and Outcomes:**

---
