#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> readFile(string filename)
{
    vector<string> input;

    ifstream inputFile(filename);
    if (inputFile.is_open())
    {
        string line;
        while (getline(inputFile, line))
        {
            input.push_back(line);
        }
        inputFile.close();
    }
    else
    {
        cout << "Unable to open file" << endl;
    }
    return input;
}

int main()
{
    vector<string> input = readFile("input.txt");
    vector<string> transposed;

    for (int j = 0; j < input[0].size(); j++)
    {
        string column = "";
        for (int i = 0; i < input.size(); i++)
        {
            column += input[i][j];
        }
        transposed.push_back(column);
    }

    string message = "";

    for (string s : transposed)
    {
        map<char, int> freq;
        for (char c : s)
        {
            freq[c]++;
        }

        char mostCommonChar;
        int highestFreq = 1000;
        for (auto p : freq)
        {
            if (p.second < highestFreq)
            {
                highestFreq = p.second;
                mostCommonChar = p.first;
            }
        }
        message += mostCommonChar;
    }

    cout << message << endl;

    return 0;
}
