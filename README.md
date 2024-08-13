# LLM-RAG-Chatbot-With-LangChain-and-Neo4j

Developing... 


# Design the Chatbot

![Architecture and data flow for the hospital system chatbot](images/Archc.png)



This flowchart illustrates how data moves through the chatbot, starting from the user’s input query all the way to the final response. Here’s a summary of each component:

- LangChain Agent: The LangChain agent is the brain of your chatbot. Given a user query, the agent decides which tool to call and what to give the tool as input. The agent then observes the tool’s output and decides what to return to the user—this is the agent’s response.

- Neo4j AuraDB: You’ll store both structured hospital system data and patient reviews in a Neo4j AuraDB graph database. You’ll learn all about this in the next section.

- LangChain Neo4j Cypher Chain: This chain tries to convert the user query into Cypher, Neo4j’s query language, and execute the Cypher query in Neo4j. The chain then answers the user query using the Cypher query results. The chain’s response is fed back to the LangChain agent and sent to the user.

- LangChain Neo4j Reviews Vector Chain: This is very similar to the chain you built in Step 1, except now patient review embeddings are stored in Neo4j. The chain searches for relevant reviews based on those semantically similar to the user query, and the reviews are used to answer the user query.

- Wait Times Function: Similar to the logic in Step 1, the LangChain agent tries to extract a hospital name from the user query. The hospital name is passed as input to a Python function that gets wait times, and the wait time is returned to the agent.