#!/usr/bin/env python
"""Optimized LPT algorithm (Longest Processing Time).

Description:
An Optimized LPT algorithm schedules jobs on processors such that loads on
the processors are almost equal and uses minimum number of processors.

Advantages:
1. Better resource usage
2. Almost equal run times on processors

Bottleneck and Dependency:
1. The upper bound of processors is dependent on largest task by time
"""
import pprint
from lpt import LPT
from math import ceil


DELIMITER1 = '\n' + '*' * 50 + '\n'
DELIMITER2 = '-' * 50 + '\n'


class OptimizedLPT(object):
    """Implementation of Optimized LPT algorithm (Longest Processing Time)."""

    def __init__(self, jobs, processors):
        """Initializing with J Jobs, M Processors, N Optimal Processors."""
        self.jobs = jobs
        self.processors = processors

    def _get_optimal_processors(self):
        """Find the Optimal Number of Processors required for Jobs.

        Step 1: Find the job with max time
        Step 2: Find the time to execute all jobs
        Step 3: Find the ideal number of processors required for an
                        almost equal load bounded by max time job.
        Step 4: If the available processors are lower than ideal number
                        of processors, use the current number of processors.
                        Else, use the ideal number of processors are optimal.
        """
        maxjob = float(max(self.jobs))
        total = float(sum(self.jobs))
        ideal = int(ceil(total / maxjob))

        if ideal < self.processors:
            return ideal

        return self.processors

    def run(self):
        """Run the Optimized LPT Algorithm."""
        optimal_processors = self._get_optimal_processors()
        lpt = LPT(self.jobs, optimal_processors)
        scheduled_jobs, loads = lpt.run()

        diff = self.processors - optimal_processors
        for item in range(diff):
            scheduled_jobs.append([])
            loads.append(0)

        return scheduled_jobs, loads


def test_lpt_zero():
    """Testing Optimized LPT algorithm with a basic non repeated jobs."""
    jobs = [3, 1, 6, 4, 5, 2]
    processors = [2, 4, 6, 8]

    print DELIMITER1
    print "Jobs: {}".format(pprint.pformat(jobs))

    for processor in processors:
        print DELIMITER2
        print "Processor: {}".format(processor)
        opt_lpt = OptimizedLPT(jobs, processor)
        scheduled_jobs, loads = opt_lpt.run()
        print "Scheduled Jobs: {}".format(pprint.pformat(scheduled_jobs))
        print "Loads: {}".format(pprint.pformat(loads))
        print DELIMITER2

    print DELIMITER1


def test_lpt_one():
    """Testing Optimized LPT algorithm w/ a medium set of non repeated jobs."""
    jobs = [507, 367, 300, 91, 82, 77, 50, 29, 26, 14, 13, 12,
            12, 11, 10, 8, 6, 3]
    processors = [2, 4, 6, 8]

    print DELIMITER1
    print "Jobs: {}".format(pprint.pformat(jobs))

    for processor in processors:
        print DELIMITER2
        print "Processor: {}".format(processor)
        opt_lpt = OptimizedLPT(jobs, processor)
        scheduled_jobs, loads = opt_lpt.run()
        print "Scheduled Jobs: {}".format(pprint.pformat(scheduled_jobs))
        print "Loads: {}".format(pprint.pformat(loads))
        print DELIMITER2

    print DELIMITER1


def test_lpt_two():
    """Testing Optimized LPT algorithm.

    Testing with a medium set of jobs with repititions.
    """
    jobs = [300, 15, 300, 17, 27, 300, 149, 12, 300, 5, 79, 19,
            4, 8, 5, 18, 5, 5, 10, 7, 9, 5, 11, 5, 301, 5, 7, 300,
            127, 300, 9, 7, 9, 8]
    processors = [2, 4, 6, 8]

    print DELIMITER1
    print "Jobs: {}".format(pprint.pformat(jobs))

    for processor in processors:
        print DELIMITER2
        print "Processor: {}".format(processor)
        opt_lpt = OptimizedLPT(jobs, processor)
        scheduled_jobs, loads = opt_lpt.run()
        print "Scheduled Jobs: {}".format(pprint.pformat(scheduled_jobs))
        print "Loads: {}".format(pprint.pformat(loads))
        print DELIMITER2

    print DELIMITER1


def test_lpt_three():
    """Testing Optimized LPT algorithm.

    Testing with a large set of jobs with repititions.
    """
    jobs = [13, 12, 12, 6, 18, 11, 1, 301, 51, 3, 8, 6, 169, 13, 8,
            2, 2, 8, 300, 29, 7, 11, 12, 26, 19, 1, 10, 39, 7, 6, 19,
            4, 50, 11, 300, 36, 106, 4, 13, 3, 7, 8, 300, 7, 8, 36, 29,
            16, 19, 35, 300, 68, 11, 5, 302, 36, 9, 4, 9, 38, 6, 2, 18,
            21, 7, 41, 8, 12, 9, 7, 35, 7, 1, 300, 10, 110, 13, 302, 14,
            80, 301, 302, 7, 19, 7, 12, 303, 12, 33, 53, 6, 21, 300, 302,
            75, 1, 7, 14, 62, 2, 13, 302, 76, 102, 2, 8, 12, 1, 37, 128,
            7, 5, 8, 6, 32, 300, 13, 7, 6, 11, 300, 7, 128, 1, 7, 303, 1,
            12, 302, 12, 63, 22, 12, 420, 32, 36, 1, 12, 32, 1, 62, 7, 7,
            301, 19, 2, 36, 11, 11, 111, 12, 10, 1, 300, 131, 18, 177, 11,
            3601, 7, 11, 31, 54, 7, 26, 13, 300, 71, 300, 301, 61, 1, 13,
            10, 12, 8, 20, 3, 28, 2, 1, 8, 301, 12, 300, 12, 1, 5, 6, 18,
            102, 300, 13, 1, 13, 17, 8, 13, 10, 300, 7, 12, 52]
    processors = [2, 4, 6, 8]

    print DELIMITER1
    print "Jobs: {}".format(pprint.pformat(jobs))

    for processor in processors:
        print DELIMITER2
        print "Processor: {}".format(processor)
        opt_lpt = OptimizedLPT(jobs, processor)
        scheduled_jobs, loads = opt_lpt.run()
        print "Scheduled Jobs: {}".format(pprint.pformat(scheduled_jobs))
        print "Loads: {}".format(pprint.pformat(loads))
        print DELIMITER2

    print DELIMITER1
