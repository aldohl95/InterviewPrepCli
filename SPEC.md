Project Overview

InterviewPrep CLI is designed to be a personal interview preparation assistant for software engineering students.

The application tracks coding practice, identifies weak topics, schedules reviews using spaced repetition, and provides insightful progress reports. By centralizing interview preparation in one tool, users can study more efficiently and monitor their growth over time.

1. Problem Tracker

Store and organize coding problems by:

Problem name
Difficulty
Topic(s)
Platform (LeetCode, HackerRank, etc.)
Date solved
Time to solve
Confidence rating
Notes

2. Daily Study Planner

Generate a personalized daily practice session based on:

Weak topics
Upcoming review dates
User-defined goals (e.g., "3 problems today")
Mix of new and review problems

3. Spaced Repetition Engine

Automatically schedule concept reviews based on previous performance.

If a topic is difficult, it appears more frequently. If mastered, reviews become less frequent.

Track concepts such as:

Hash Maps
DFS
BFS
Union Find
Dynamic Programming
Binary Search
Sliding Window
Two Pointers

4. Progress Dashboard

Display meaningful statistics such as:

Problems solved
Problems solved this week
Current streak
Longest streak
Average solving time
Success rate by topic
Topic mastery percentages
Difficulty distribution

5. Recognition Sentence Library

Store and review concise "recognition sentences" for algorithmic patterns.

Technology Stack
Language
  Python 3.12+
CLI Framework
  Click
Database
  SQLite
ORM / Database Access
  SQLAlchemy
Data Processing
  pandas (for exporting reports)
Terminal UI
  Rich
Testing
  pytest
Configuration
  TOML
Packaging
  pyproject.toml

Expected Folder Structure

interviewprep-cli/
│
├── interviewprep/
│   ├── cli.py
│   ├── database.py
│   ├── models.py
│   ├── planner.py
│   ├── tracker.py
│   ├── review.py
│   ├── dashboard.py
│   ├── reports.py
│   ├── utils.py
│   └── config.py
│
├── tests/
│
├── docs/
│
├── README.md
├── SPEC.md
├── pyproject.toml
└── .github/
    └── workflows/

Example Commands

prep add-problem

prep review

prep dashboard

prep study-plan

prep add-recognition

prep export

prep stats

prep streak

prep quiz

prep report