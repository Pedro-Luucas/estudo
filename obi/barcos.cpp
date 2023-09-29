#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int dfs(vector<vector<pair<int,int>>>& adjList, int initial, int final, vector<int>& visited, int minWeight = 100000) {
    if (initial == final) {
        return minWeight;
    }

    int localSize = (adjList[initial].size())+1;

    visited.push_back(initial);

    int highestMinWeight = 0;

    for (int i = 0; i < localSize; i++) {
        int currentWeight = adjList[initial][i].second;

        if (count(visited.begin(), visited.end(), adjList[initial][i].first)) {
            continue;
        }

        int val = dfs(adjList, adjList[initial][i].first, final, visited, min(minWeight, currentWeight));
        highestMinWeight = max(highestMinWeight, val);
    }
    return highestMinWeight;
}

int main() {
    int numNodes, numEdges;
    cin >> numNodes >> numEdges;
    vector<vector<pair<int,int>>> adjList(numNodes + 1);
    vector<int> visited(numNodes + 1);
    for (int i = 0; i < numEdges; i++) {
        int startNode, endNode, weight;
        cin >> startNode >> endNode >> weight;
        adjList[startNode].push_back(make_pair(endNode, weight));
        adjList[endNode].push_back(make_pair(startNode, weight));
    }
    int numQueries;
    cin >> numQueries;
    for (int i = 0; i < numQueries; i++) {
        int startNode, endNode;
        cin >> startNode >> endNode;
        cout << dfs(adjList, startNode, endNode, visited) << endl;
        visited.clear();
    }
}