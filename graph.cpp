#ifndef GRAPH_H_
#define GRAPH_H_

#include <vector>
#include <stack>
#include <string>
#include <iostream>

using namespace std;

enum Status {
	NOT_VISITED,
	VISITED
};

class Node;

class Edge{
	private:
		Node *nodeA;
		Node *nodeB;
		unsigned cost;

	public:
		Edge(Node *node_a, Node *node_b, unsigned inCost){
			nodeA = node_a;
			nodeB = node_b;
			cost = inCost;
		}

		Node* getNodeA(){
			return nodeA;
		}

		Node* getNodeB(){
			return nodeB;
		}

		unsigned getCost(){
			return cost;
		}
};

class Node{
	private:
		string name;
		vector<Edge> edgeList;
		enum Status status;

	public:
		Node(string id){
			name = id;
			status = NOT_VISITED;
		}

		~Node(){
			nodeList.clear();
		}

		enum Status getStatus(){
			return status;
		}

		void setStatus(enum Status st){
			status = st;
		}

		string getName(){
			return name;
		}

		void addNode(Node *node, unsigned cost){
			Edge newEdge(this, node, cost);
			edgeList.push_back(newEdge);
		}

		vector<Edge>& getNodeList(){
			return edgeList;
		}
};

class Graph{
	private:
		vector<Node*> nodeList;
	
		void clearVisited(){
		for(int i = 0; i < nodeList.size(); i++){
			nodeList[i]->setStatus(NOT_VISITED);
		}
	}

	void addNewNode(Node *nNode){
		nodeList.push_back(nNode);
	}

	Node* findNodeByName(string name){
		for(int i = 0 ; i < nodeList.size() ; i++){
			if(nodeList[i]->getName() == name){
				return nodeList[i];
			}
		}
		return NULL;
	}

	public:
		Graph(){
		}

		~Graph(){
		for(int i=0 ; i < nodeList.size() ; i++){
			delete nodeList[i];
		}
		nodeList.clear();
	}

};

int main () {
	Graph graph();
	Node node_a("foo");
	Node node_b("bar");
}
#endif
