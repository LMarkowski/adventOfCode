#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

bool compare(pair<char, int> a, pair<char, int> b)
{
    if (a.second == b.second)
    {
        // If counts are equal, sort alphabetically
        return a.first < b.first;
    }
    return a.second > b.second; // Sort by count in descending order
}

string checkSum(string input)
{
    map<char, int> charCount;

    // Count the occurrences of each character
    for (char c : input)
    {
        charCount[c]++;
    }

    // Convert the map to a vector of pairs (character, count)
    vector<pair<char, int> > charCountVector;
    for (const auto &pair : charCount)
    {
        charCountVector.push_back(pair);
    }

    // Sort the vector based on frequency and then alphabetically
    sort(charCountVector.begin(), charCountVector.end(), compare);

    string checkSum = "";

    for (int i = 0; i < 5; i++)
    {
        checkSum += charCountVector[i].first;
    }

    return checkSum;
}

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

    vector<vector<string> > rooms;

    for (string room : input)
    {
        vector<string> room_data;

        size_t openBracketPos = room.find('[');
        size_t closeBracketPos = room.find(']');
        string checkSum = room.substr(openBracketPos + 1, closeBracketPos - openBracketPos - 1);
        room = room.substr(0, room.length() - 7);

        size_t dashPos = room.rfind('-');
        string sectorID = room.substr(dashPos + 1, room.length() - dashPos - 1);
        room = room.substr(0, dashPos);

        for (size_t i = 0; i < room.length(); i++)
        {
            if (room[i] == '-')
            {
                room.erase(i, 1); // Erase 1 character at position i
                i--;              // Decrement i to account for the removed character
            }
        }

        room_data.push_back(room);
        room_data.push_back(sectorID);
        room_data.push_back(checkSum);
        rooms.push_back(room_data);
    }

    int sectorIDSum = 0;

    for (vector<string> room : rooms)
    {
        // cout << "Name: " << room[0] << endl;
        // cout << "Sector ID: " << room[1] << endl;
        // cout << "Checksum: " << room[2] << endl;

        string calculatedCheckSum = checkSum(room[0]);
        // cout << "Calculated checksum: " << calculatedCheckSum << endl;

        if (calculatedCheckSum == room[2])
        {
            sectorIDSum += stoi(room[1]);
        }
    }

    cout << "Sum of sector IDs: " << sectorIDSum << endl;

    // Part 2
    
    for (vector<string> room : rooms)
    {
        string decryptedName = "";
        int sectorID = stoi(room[1]);

        for (char c : room[0])
        {
            int charIndex = c - 'a';
            charIndex += sectorID;
            charIndex %= 26;
            charIndex += 'a';
            decryptedName += charIndex;
        }

        if (decryptedName.find("north") != string::npos)
        {
            cout << "Sector ID of North Pole objects: " << sectorID << endl;
        }
    }

    return 0;
}
