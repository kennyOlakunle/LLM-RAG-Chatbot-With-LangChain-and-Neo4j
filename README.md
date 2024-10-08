# LLM-RAG-Chatbot-With-LangChain-and-Neo4j

Developing... 


# Design the Chatbot

![Architecture and data flow for the hospital system chatbot](images/Archc.png)



This flowchart illustrates how data moves through the chatbot, starting from the user’s input query all the way to the final response. Here’s a summary of each component:

- LangChain Agent: The LangChain agent is the brain of the chatbot. Given a user query, the agent decides which tool to call and what to give the tool as input. The agent then observes the tool’s output and decides what to return to the user—this is the agent’s response.

- Neo4j AuraDB: The DB stores both structured hospital system data and patient reviews in a Neo4j AuraDB graph database.

- LangChain Neo4j Cypher Chain: This chain tries to convert the user query into Cypher, Neo4j’s query language, and execute the Cypher query in Neo4j. The chain then answers the user query using the Cypher query results. The chain’s response is fed back to the LangChain agent and sent to the user.

- LangChain Neo4j Reviews Vector Chain: The patient review embeddings are stored in Neo4j. The chain searches for relevant reviews based on those semantically similar to the user query, and the reviews are used to answer the user query.

- Wait Times Function: The LangChain agent tries to extract a hospital name from the user query. The hospital name is passed as input to a Python function that gets wait times, and the wait time is returned to the agent.


![Hospital system graph database design](images/Hospital_sys_design.png)

This diagram shows all of the nodes and relationships in the hospital system data. One useful way to think about this flowchart is to start with the Patient node and follow the relationships. A Patient has a visit at a hospital, and the hospital employs a physician to treat the visit which is covered by an insurance payer.


![Hospital system node properties](images/Hospital_sys_design.png)

One notable difference is that Review nodes have an embedding property, which is a vector representation of the patient_name, physician_name, and text properties. This allows you to do vector searches over review nodes
