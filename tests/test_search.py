import unittest 
from src.main import search_notes

class TestStudyLensSearch(unittest.TestCase):
     def setUp(self):
         # Sample notes for testing
         self.paragraphs = [
            "BFS explores nodes. BFS uses a queue. BFS visits levels.",
            "DFS uses a stack data structure.",
            "Machine Learning learns patterns from data."
        ]
     def test_keyword_search(self):
        results = search_notes("BFS", self.paragraphs)
        self.assertEqual(len(results), 1)

     def test_case_insensitive_search(self):
          results = search_notes("bfs",self.paragraphs)
          self.assertEqual(len(results), 1)

     def test_no_matching_results(self):
        results = search_notes("Java", self.paragraphs)
        self.assertEqual(results, [])

     def test_empty_query(self):
        results = search_notes("", self.paragraphs)
        self.assertEqual(results, [])

     def test_result_ranking(self):
        results = search_notes("BFS", self.paragraphs)
        self.assertEqual(results[0][1], 3)


if __name__ == "__main__":
    unittest.main()

