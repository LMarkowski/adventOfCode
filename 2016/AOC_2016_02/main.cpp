#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    vector<string> input;

    ifstream inputFile("input.txt");
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

    int x = 1, y = 1; // Starting position
    int keypad[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}};

    for (string line : input)
    {
        for (char c : line)
        {
            switch (c)
            {
            case 'U':
                if (y > 0)
                {
                    y--;
                }
                break;
            case 'D':
                if (y < 2)
                {
                    y++;
                }
                break;
            case 'L':
                if (x > 0)
                {
                    x--;
                }
                break;
            case 'R':
                if (x < 2)
                {
                    x++;
                }
                break;
            }
        }
        cout << keypad[y][x];
    }
    cout << endl;

    // Part 2

    x = 0, y = 2; // Starting position
    char keypad2[5][5] = {
        {' ', ' ', '1', ' ', ' '},
        {' ', '2', '3', '4', ' '},
        {'5', '6', '7', '8', '9'},
        {' ', 'A', 'B', 'C', ' '},
        {' ', ' ', 'D', ' ', ' '}};

    for (string line : input)
    {
        for (char c : line)
        {
            switch (c)
            {
            case 'U':
                if (y > 0 && keypad2[y - 1][x] != ' ')
                {
                    y--;
                }
                break;
            case 'D':
                if (y < 4 && keypad2[y + 1][x] != ' ')
                {
                    y++;
                }
                break;
            case 'L':
                if (x > 0 && keypad2[y][x - 1] != ' ')
                {
                    x--;
                }
                break;
            case 'R':
                if (x < 4 && keypad2[y][x + 1] != ' ')
                {
                    x++;
                }
                break;
            }
        }
        cout << keypad2[y][x];
    }
    cout << endl;

    return 0;
}
