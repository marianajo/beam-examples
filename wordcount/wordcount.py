"""Wordcount example.

This is a batch processing example, where all the data is bounded in a
text file. The pipeline finds all the words and counts how many times
each word appears in the text. Then it writes tuples (word, count) to
a file.

The text example is the tale "O Enfermeiro", by Machado de Assis,
in Portuguese. This tale is in Public Domain.
"""
import apache_beam as beam
import re

with beam.Pipeline() as p:
    totals = (p | beam.io.ReadFromText('text.txt')
              | beam.FlatMap(lambda line: re.findall(r'\w+', line))
              | beam.combiners.Count().PerElement()
              | beam.io.WriteToText('output'))
