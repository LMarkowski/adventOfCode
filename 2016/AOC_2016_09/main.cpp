#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <regex>

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

string decompress(string input)
{
    regex marker("\\((\\d+)x(\\d+)\\)");
    smatch match;
    regex_search(input, match, marker);
    if (match.empty())
    {
        return input;
    }
    int length = stoi(match[1]);
    int repeat = stoi(match[2]);
    string decompressed = input.substr(match.position(0) + match.length(), length);
    for (int i = 0; i < repeat; i++)
    {
        decompressed += decompress(decompressed);
    }
    return decompressed;
}

int main()
{
    vector<string> input = readFile("input.txt");

    for (string line : input)
    {
        cout << decompress(line) << endl;
    }
    return 0;
}
