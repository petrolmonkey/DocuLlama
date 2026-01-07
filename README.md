# Chatbot
A chatbot for looking up information in owner's manuals

## Objective
Since I like to work with my hands, I have collected a lot of tools and manuals over the years. Inevitably, something breaks - like the lawnmower not starting - and then I have to find the manual and sift through the pages to find what I need; it can be a chore 

One way to make this process streamlined, is to download all the manuals and use a chatbot to locate the information. I needed a chatbot interface but I had no experience designing in HTML or CSS. It was daunting. So I decided to break it down into chunks. 

## Version Overview
1. What did you learn?
2. What did you add?


***********************************************************************************************
Show “Evolution"
Show reviewers growth without having to browse multiple repos
Explains each version in 1–2 bullet points (what you learned, what you added, what changed).
**********************************************************************************************
 
### Chatbot v1 - How to use Streamlit
I discovered I could use Python, a language I am familiar with, to create the front end with its Streamlit library. This part was about getting familiar with the librarie's methods; I learned how to accept user input, generate a pre-defined response and display it.
* [chatbot v1](./v1-echo-bot) ➡️

### chatbot v2 - Connecting an LLM
The first 2 examples.... how to obtain and load an API key to use an LLM.
* [chatbot v2](./v2-doc-qa) ➡️

### chatbot v3
This version converts several instruction manuals into a searchable data structure and makes it accessible through the chatbot interface. The predefined responses in the script were replaced with a query engine.
* [chatbot v3](./v3-doc-qa) ➡️ 
