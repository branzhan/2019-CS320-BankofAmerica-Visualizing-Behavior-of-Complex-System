# 2019-CS320-BankofAmerica-Visualizing-Behavior-of-Complex-System 

Development by: Brian Zhang, Saurav Chatterjee, Zachary Stephens

This Capstone project, proposed by Michael Karafotis (michael.karafotis@bofa.com), demands a visualization of interconnected data nodes across five primary levels.

These five layers are Infrastructure, Application, Business, Service, and Process. 
Ultimately, these layers form a sort of abstraction stack, wherein Business defines Applications within the Infrastructure, and Businesses are made up of Services and Processes.
The primary goal is to generate a model in which one can observe the correlations between Key Performance Indicators of components both within layers and between layers. 
Namely, if there is a failure at the Service level, the model will relate the shift in KPIs within the Service to the Business and Application it belongs too.
Similarly, the model should be able to analyze more dynamically the relationship between the failure in the Service and any other failures that may arise, regardless of which things may intuitively be linked to one another. 

Given the grand scope of this dataset, we will need to communicate with the sponsor on what the best way to portray all of this data is. 
As the dataset grows, we will need to implement features which manage scalability, such as allowing viewing by slices of interrelated nodes.



*NOTE*
--------------------------------------------------------------------------------------------------------------------------------
 Below are short explanations for the folders in the github. Many of the folders, expecially folders that contain code, have Read me files that explain the setup/use. 
 
 * Code  ----> Early development code that contains the initial observable code and html page. Not final web application/observable code. For Observable code, check Observable folder. For web page, check public folder. 
 
 * Documentation ----> Much of this folder is dedicated to the required documentation for the capstone project. However, many of the documents in the folder are project specific and contain early design notes. 
 
 * Notes and Research ----> Early meeting notes before the format switched and notes about visualization.
 
 * Observable ----> Code for observable and the JavaScript files.
 
 * Presentation ----> Would have contained the presentation, but the format changed and the video was instead uploaded. 
 
 * Status Report ----> Status reports that contain work done, work need to be done, and challanges. 
 
 * flask ----> Contains the flask implementation and how to set it up in the read me file. 
 
 * flask1 ----> Similiar code with minor changes. 
 
 * public ----> Contains the web page code: html, css, and images. 
 
 * Python ----> Folder only contains the data scrubbed after the random data was given from bank and json files from the data. 
 
 -----------------------------------------------------------------------------------------------------------------------------------
 
 Contact information: 
 
 * Saurav Chatterjee - chatterjees3@vcu.edu
 * Brian Zhang - zhangb8@mymail.vcu.edu 
 * Zachary Stephens - stephenszc@mymail.vcu.edu 


