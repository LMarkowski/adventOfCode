#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <regex>

using namespace std;

pair<string, string> splitIP(string input)
{
    string outside, inside;
    bool isInside = false;

    for (char c : input)
    {
        if (c == '[')
        {
            outside += '_';
            isInside = true;
            continue;
        }
        if (c == ']')
        {
            inside += '_';
            isInside = false;
            continue;
        }

        if (isInside)
        {
            inside += c;
        }
        else
        {
            if (c != '[')
            {
                outside += c;
            }
        }
    }

    return make_pair(outside, inside);
}

bool containsABBA(string s)
{
    for (int i = 0; i < s.length() - 3; i++)
    {
        if (s[i] == s[i + 3] && s[i + 1] == s[i + 2] && s[i] != s[i + 1])
        {
            return true;
        }
    }
    return false;
}

bool isSSL(string outside, string inside)
{
    for (int i = 0; i < outside.length() - 2; i++)
    {
        if (outside[i] == outside[i + 2] && outside[i] != outside[i + 1])
        {
            string aba = outside.substr(i, 3);
            string bab = "";
            bab += aba[1];
            bab += aba[0];
            bab += aba[1];
            if (inside.find(bab) != string::npos)
            {
                return true;
            }
        }
    }
    return false;
}

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

    int count = 0;

    for (string line : input)
    {
        pair<string, string> out_in = splitIP(line);
        if (containsABBA(out_in.first) && !containsABBA(out_in.second))
        {
            count++;
        }
    }

    cout << "Part 1: " << count << endl;

    count = 0;
    for (string line : input)
    {
        pair<string, string> out_in = splitIP(line);
        if (isSSL(out_in.first, out_in.second))
        {
            count++;
        }
    }

    cout << "Part 2: " << count << endl;

    return 0;
}
