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

int printScreen(bool screen[6][50])
{
    int count = 0;
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 50; j++)
        {
            if (screen[i][j])
            {
                count++;
                cout << "#";
            }
            else
            {
                cout << " ";
            }
        }
        cout << endl;
    }
    return count;
}

int main()
{
    vector<string> input = readFile("input.txt");

    bool screen[6][50] = {{false}};

    regex rectRegex("rect ([0-9]+)x([0-9]+)");
    regex rotateRowRegex("rotate row y=([0-9]+) by ([0-9]+)");
    regex rotateColumnRegex("rotate column x=([0-9]+) by ([0-9]+)");

    for (string line : input)
    {
        smatch match;
        if (regex_search(line, match, rectRegex))
        {
            int width = stoi(match[1]);
            int height = stoi(match[2]);
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    screen[i][j] = true;
                }
            }
        }
        else if (regex_search(line, match, rotateRowRegex))
        {
            int row = stoi(match[1]);
            int amount = stoi(match[2]);
            bool temp[50];
            for (int i = 0; i < 50; i++)
            {
                temp[(i + amount) % 50] = screen[row][i];
            }
            for (int i = 0; i < 50; i++)
            {
                screen[row][i] = temp[i];
            }
        }
        else if (regex_search(line, match, rotateColumnRegex))
        {
            int column = stoi(match[1]);
            int amount = stoi(match[2]);
            bool temp[6];
            for (int i = 0; i < 6; i++)
            {
                temp[(i + amount) % 6] = screen[i][column];
            }
            for (int i = 0; i < 6; i++)
            {
                screen[i][column] = temp[i];
            }
        }
    }

    cout << "Part 1: " << endl
         << printScreen(screen) << endl;

    return 0;
}
