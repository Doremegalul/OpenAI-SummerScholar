/****************************
Templated created by Kazumi Slott
CS311

Your name: Minh Tran
Your programmer number: 37
Hours spent: 24 hours (Lets go, I wasted my life on this)
Any difficulties?: Memory corruption, it is floating pointer that I need to keep in track of.
*****************************/
#ifndef GRAPH_H
#define GRAPH_H
#include <iostream>
#include <queue>
#include <list>
#include <string>
#include <stack>
#include "minHeap-graph.h"

using namespace std;

struct Place{
  int num;
  string abr;
  string name;
  int population;
  int elevation;
};

class graph;

class edge
{
	friend class graph; //You want to access the private members of edge class from graph class
	int neighbor; //adjacent vertex
	int wt; //weight of the edge
	public:
		edge() { neighbor = -999, wt = -999;};
		edge(int u, int w) {neighbor = u, wt = w;}; /* set data members */
};

class graph
{
	int num_ver; //the total number of vertices in the graph
	list<edge*>* ver_ar; //pointer to the dynamic array that holds linked lists. The element of a node in a linked list is a pointer to an edge object 
						 //Let's use the library's list class. It is actually a doubly linked list. 
	int nextUnvisitedNodes(int* num, int start,int s);
	void DFT_helper(int v, int& i, int* num, queue<string>& q);
	public:
		graph(int V);
		~graph();
		void addEdge(int v, int u, int w=1);  //If the weight is not given, 1 is used for wt.
		void BFT(int start);
		void DFT(int start);
		void DijkstraShortestPath(int start, int dest, Place cityData[]);
};

//constructor: num is the number of vertices
graph::graph(int num)
{
	//Initialize the num
	this->num_ver = num;
	
	//make a dynamic array with num slots where each slot holds a list object. 
	ver_ar = new list<edge*>[num_ver];
	//The element of a node in the linked list is a pointer to an edge object 
}

//destroy all the edge objects created in heap
graph::~graph()
{ 
	for(int i = 0; i < num_ver; i++)
    {
		//For each vertex in ver_ar
		for(list<edge*>::iterator u = ver_ar[i].begin(); u != ver_ar[i].end(); u++)
		{	
			//go through each node in the linked list. The element field of each node points to an edge object created with "new". You need to delete these. 
			delete *u;
		}
    }
	
	//The library's list class has a destructor. All nodes belonging to the list will be destroyed by the destructor.
	//https://www.cplusplus.com/reference/list/list/~list/
	
	delete [] ver_ar; //destroy the ver_ar dynamic array
}


//add an edge from v to u with weight w into the graph
void graph::addEdge(int v, int u, int w)
{
	//We are using the list class from the library. Which member function do you need to use to add a node at the end of the list?
	//https://www.cplusplus.com/reference/list/list/
  
	//Don't create an edge object statically, then it would get destroyed as soon as you leave this function. You need to create an edge object dymamically in heap, which will remain in heap even after you leave this function.. Remember "new" operator returns the memory address of the newly created object.
	//I have one line of code in this function.
	ver_ar[v].push_back(new edge(u, w));
}

//I decided to make this function a stand alone function. It doesn't have anything to do with the graph class.                                
template<class T>
void displayQueue(queue<T>& q)
{
	//Not empty
	while(!q.empty())
    {
		cout << q.front() << ",";
		q.pop();
    }
}

//start Traversal at start
void graph::DFT(int start)
{
	//The algorithm is in my lecture notes.
  
	//I made dynamic array called "num"
	int* num = new int[num_ver];
  
	//I created a queue object of string data type from the library's queue class to save all the paths.
	queue<string> q;
	
	//Going through the dynamic array to make it not visited yet
	for(int i = 0; i < num_ver; i++)
    {
      num[i] = 0;
    }
	
	int i = 1;
	int temp = start; //A temporary variable to prevent any problem with start.
	
	//I used do-while
	do
	{
		DFT_helper(temp, i, num, q);
		//I am calling nextUnvisitedNodes() to see if there are more unvisited nodes.
		temp = nextUnvisitedNodes(num, temp, temp + 1);
	}while(temp != -1);
	
	//You could call displayQueue() implemented above to display all the paths. 
	displayQueue(q);
	cout << endl;
	
	//Don't forget to destroy the dynamic array
	delete [] num;
}

//I made the following function to see if there are still unvisited nodes. Start checking at s, which is the one after the vertext we started last time                       
//num points to an array containing visit numbers. 0 indicates, the vertex hasn't been visited yet.                                           
//s is the vertext right after the vertex we started last time  
int graph::nextUnvisitedNodes(int* num, int start, int s)
{
	//go through the num array to see if you find a vertext with num=0. If so, return the index. If all visited, return -1.
	//don't start from index 0!
	//Althought this function may be called multiple times because there may be multiple disconnected graphs, we are checking each vertex only once.	  
	
	for(int i = s; i != start; i = (i + 1) % num_ver)
    {
		if(num[i] == 0)
		{
			return i;
		}
    }
	
	return -1; 
}

void graph::DFT_helper(int v, int& i, int* num, queue<string>& q)
{
	//The algorithm is in my lecture notes
	num[v] = i++;
  
	//cout << char(v + 'A') << "-->";
	cout << v << " ";
  
	//The following shows how to iterate the library's linked list. You use an iterator.                                                                                                                     
	//https://www.cplusplus.com/reference/list/list/end/          
  
  
	//iterator class is nested inside list class.
	for (list<edge*>::iterator u = ver_ar[v].begin(); u != ver_ar[v].end(); u++)
	{
		//From the example on https://www.cplusplus.com/reference/list/list/end.
		//Notice *u gives you the element of the node pointed to by u. The element is a pointer to an edge object.          
		
		if (num[((*u)->neighbor)] == 0)//If the node is this number go to this section.
		{
			//Between * and -> operator, -> has higher precedence. You need to use () around *u to get the element first.
			q.push(to_string(v) + "->" + to_string((*u)->neighbor));	
			//push each path e.g. 0->1 into q. to_string(int) converts the int to a string.                                                                                                                       
			//to_string() is in c++11, so compile with the option. g++ -std=c++11 graphClient.cpp 
			DFT_helper(((*u)->neighbor), i, num, q);
		} 
	}
}

/*********************************************************************************************
**********************************************************************************************                           
Compile with a c++11 option if you are using to_string()                                                                                                                                             
g++ -std=c++11 graphClient.cpp                                                                                                                                                              
**********************************************************************************************      
*********************************************************************************************/

//start is the index for the start vertex
void graph::BFT(int start)
{
	//The algorithm is in my lcture notes
  
	//Use the queue class from the library
	queue<int> q;
  
	//I used another queue of strings to save all the paths.
	queue<string> s;
  
	//More dynamic array
	int *num = new int[num_ver]; 
  
	for(int i = 0; i < num_ver; i++)
	{
		num[i] = 0;
	}
  
	//The first vertex visited gets 1
	int i = 1;
	int temp = start; //A temporary variable to prevent anything happen to start
  
	//I used do-while to visit all unconnected graphs. Call nextUnvisitedNodes() to check to see if there are more unvisited verteces.
	do
	  {
		num[temp] = i++;
		q.push(temp);
		while(!q.empty())
		{
			temp = q.front();//Using the temporary variable to save the front, please...
			q.pop();
			cout << temp << " ";//Will show the contents.
			
			for(list<edge*>::iterator u = ver_ar[temp].begin(); u != ver_ar[temp].end(); u++)
			{
				if(num[(*u)->neighbor] == 0)
				{
					num[(*u)->neighbor] = i++;
					q.push((*u)->neighbor);
					s.push(to_string(temp) + "->" + to_string((*u)->neighbor));
				}
			}
		}
		temp = nextUnvisitedNodes(num, temp, temp + 1);
	  }while(temp != -1);
 
	//Check the manual to figure out what member functions of the queue class you need to use.                                                                                                               
	//https://www.cplusplus.com/reference/queue/queue/     
	
	//You could call show all paths by calling displayQueue()            
	displayQueue(s);
	cout << endl;
 
	//Don't forget to destroy the dynamic array if you used one
	delete[] num;
}

//dijkstra's algorithm calculates the shortest distance from start to every other vertex
//This stand alone function shows the shortest path from start to destination in the following format.
//  The shortest path from 3 to 5 is 3 0 4 5
//  The distance is 8
void showShortestDistance(int* curDist, int* predecessor, int start, int dest, Place cityData[])
{
	
	//trace the shortest path from dest back to start
	//I suggest you use either library's stack or queue. Which one will work?
	stack<int> s;
  
	int destDist = curDist[dest];
	int destNameSave = dest;
	
	while(dest != start)//Adding to the stack until reach start or A
    {
		s.push(dest);
		dest = predecessor[dest];
		if(dest == -1)
		{
			cout << "No route from " << cityData[start].name << " to " << cityData[destNameSave].name << endl;
			exit(1);
		}
    }
	s.push(dest);
	
	cout << "The shortest distance distance from " << cityData[start].name << " to " << cityData[destNameSave].name << " is " << destDist << endl;
	
	cout << "through the route: ";
	while(!s.empty())//Adding start of A to the stack (C, B, A)
    {
		cout << cityData[s.top()].name;//Print out A B C
		s.pop();
		if(!s.empty())
		{
			cout << "->";
		}
    }

	cout << endl;
}

//You don't need to change the following function.
//This function is for checking the heap and all the arrays. You may want to call it while you are developing Dijkstra's function
//This is not part of the graph class. It is made for testing anyway.
void printHeapArrays(const minHeap<int>& h, int* curDist, int* locator, int* predecessor, int num_ver)
{
	cout << "heap ------" << endl;
	cout << h << endl;  //This works if you made operator<<() to display a heap

	cout << "locator ------" << endl;
	for(int i = 0; i < num_ver; i++)
		cout << locator[i] << " ";
	cout << endl;

	cout << "curDist ------- " << endl;
	for(int i = 0; i < num_ver; i++)
		cout << curDist[i] << " ";
	cout << endl << endl;

	cout << "Predecessor ------- " << endl;
	for(int i = 0; i < num_ver; i++)
		cout << predecessor[i] << " ";
	cout << endl << endl;
}

//Dijkstra's shortest path. This function will generate a table that contains the shortest distance from start to every other vertex and the predecessor of each vertex.
void graph::DijkstraShortestPath(int start, int dest, Place cityData[])
{
	minHeap<int> toBeChecked(num_ver); //the top of this heap has the vertex with the shortest distance declare a dynamic array called curDist //contains the current shortest distance from start to every other vertex declare a dynamic array called predecessor //contains the predecessor of each vertex declare a dynamic array called locator //tells where each vertex exists within the heap. e.g. heap [v3, v1, v2, v4, v0] locator [4, 1, 2, 0, 3] <== vertext 0 can be found at index 4 in heap, vertex 3 can be found at index 0 in heap
  
	//declare a dynamic array called curDist //contains the current shortest distance from start to every other vertex
	int* curDist = new int[num_ver];
	
	//declare a dynamic array called predecessor //contains the predecessor of each vertex
	int* predecessor = new int[num_ver];
	
	//declare a dynamic array called locator //tells where each vertex exists within the heap. e.g. heap [v3, v1, v2, v4, v0] locator [4, 1, 2, 0, 3] <== vertext 0 can be found at index 4 in heap, vertex 3 can be found at index 0 in heap
	int* locator = new int[num_ver];
  
	for(int v = 0; v < num_ver; v++)//Go through this contition to fill up the current distance only.
	{
		curDist[v] = 999;
	}
	
	//to start with, locator [0, 1, 2, 3, 4, ...] 
	for(int i = 0; i < num_ver; i++) 
	{
		locator[i] = i;
	}
	
	//populate toBeChecked heap 
	//insert all vetices into toBeChecked heap: [0, 1, 2, 3, 4, ...] the numbers are vertex numbers
	for(int i = 0; i < num_ver; i++)
    {
		toBeChecked.insert(curDist, locator, i);
    }
	
	//Initialize predecessor for each vertex to -1
	for(int i = 0; i < num_ver; i++) 
	{
		predecessor[i] = -1;
	}
	
	//A lof of code here - check the algorithm in my lecture notes	
	curDist[start] = 0;
	int temp = start;
	
	while(toBeChecked.getNum() > 0)
  {
		//printHeapArrays(toBeChecked, curDist, locator, predecessor, num_ver);
		toBeChecked.fixHeap(curDist, locator, locator[temp]);
		temp = toBeChecked.getMin(curDist, locator);
     
		for(list<edge*>::iterator u = ver_ar[temp].begin(); u != ver_ar[temp].end(); u++)
		{
			if(locator[(*u)->neighbor] < toBeChecked.getNum())
			{
				if(curDist[(*u)->neighbor] > (curDist[temp] + (*u)->wt))
				{
					curDist[(*u)->neighbor] = curDist[temp] + (*u)->wt;
					predecessor[(*u)->neighbor] = temp;
					toBeChecked.fixHeap(curDist, locator, locator[(*u)->neighbor]);
				}

			}
		}
  }

    //Now currDist and predecessor have the info about the shortest distance from start to every other vertex and the predecessor of each vertex
    showShortestDistance(curDist, predecessor, start, dest, cityData); //print the result

    delete [] curDist;
    delete [] predecessor;
    delete [] locator;
}

#endif