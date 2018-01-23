#!/usr/bin/env python
"""LPT algorithm (Longest Processing Time).

Description:
A simple, often-used multiprocessor scheduling (load balancing) algorithm
is the LPT algorithm (Longest Processing Time) which sorts the jobs by its
processing time and then assigns them to the machine with the earliest
end time so far. This algorithm achieves an upper bound of 4/3 - 1/(3m) OPT.

Problem Statement:
"Given a set J of jobs where job ji has length li and a number of processors m,
what is the minimum possible time required to schedule all jobs in J on
m processors such that none overlap?"

Background:
In computer science, multiprocessor scheduling is an NP-hard optimization
problem. The applications of this problem are numerous, but are, as suggested
by the name of the problem, most strongly associated with the scheduling of
computational tasks in a multiprocessor environment.
"""
import time
import pprint

DELIMITER1 = '\n' + '*' * 50 + '\n'
DELIMITER2 = '-' * 50 + '\n'


def timing(f):
    """Decorator to check the time taken to execute a function."""
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        time_taken = (time2 - time1) * 1000.0
        print '%s function took %0.3f ms' % (f.func_name, time_taken)
        return ret
    return wrap


class LPT(object):
    """Implementation of LPT algorithm (Longest Processing Time)."""

    def __init__(self, jobs, processors):
        """Initializing with J Jobs, M Processors."""
        self.jobs = jobs
        self.processors = processors

    def run(self):
        """Run the LPT Algorithm."""
        scheduled_jobs, loads = self.lpt_algorithm()
        return scheduled_jobs, loads

    @timing
    def lpt_algorithm(self):
        """Run the LPT Algorithm.

        Steps:
        1. Sort J jobs in descending order of processing time.
        2. Create a array representing loads on each processor
           a. Initially all loads will be 0
        3. Create an array of array representing the scheduled jobs
           on each processor
           a. Initially no jobs will be scheduled on the processors
        4. Assign each job to a processor based on lowest load
        """
        # Step 1
        sorted_jobs = sorted(self.jobs, reverse=True)

        # Step 2, Step 3
        loads = []
        scheduled_jobs = []
        for processor in range(self.processors):
            loads.append(0)
            scheduled_jobs.append([])

        # Step 4
        for job in sorted_jobs:
            minloadproc = self._minloadproc(loads)
            scheduled_jobs[minloadproc].append(job)
            loads[minloadproc] += job

        return scheduled_jobs, loads

    def _minloadproc(self, loads):
        """Find the processor with the minimum load.

        Break the tie of processors having same load on
        first come first serve basis.
        """
        minload = min(loads)
        for proc, load in enumerate(loads):
            if load == minload:
                return proc


def test_lpt_zero():
    """Testing LPT algorithm with a basic non repeated jobs."""
    jobs = [3, 1, 6, 4, 5, 2]
    processors = [2, 4, 6, 8]

    print DELIMITER1
    print "Jobs: {}".format(pprint.pformat(jobs))

    for processor in processors:
        print DELIMITER2
        print "Processor: {}".format(processor)
        lpt = LPT(jobs, processor)
        scheduled_jobs, loads = lpt.run()
        print "Scheduled Jobs: {}".format(pprint.pformat(scheduled_jobs))
        print "Loads: {}".format(pprint.pformat(loads))
        print DELIMITER2

    print DELIMITER1


def test_lpt_one():
    """Testing LPT algorithm with a medium set of non repeated jobs."""
    jobs = [507, 367, 300, 91, 82, 77, 50, 29, 26, 14, 13, 12,
            12, 11, 10, 8, 6, 3]
    processors = [2, 4, 6, 8]

    print DELIMITER1
    print "Jobs: {}".format(pprint.pformat(jobs))

    for processor in processors:
        print DELIMITER2
        print "Processor: {}".format(processor)
        lpt = LPT(jobs, processor)
        scheduled_jobs, loads = lpt.run()
        print "Scheduled Jobs: {}".format(pprint.pformat(scheduled_jobs))
        print "Loads: {}".format(pprint.pformat(loads))
        print DELIMITER2

    print DELIMITER1


def test_lpt_two():
    """Testing LPT algorithm with a medium set of jobs with repititions."""
    jobs = [300, 15, 300, 17, 27, 300, 149, 12, 300, 5, 79, 19,
            4, 8, 5, 18, 5, 5, 10, 7, 9, 5, 11, 5, 301, 5, 7, 300,
            127, 300, 9, 7, 9, 8]
    processors = [2, 4, 6, 8]

    print DELIMITER1
    print "Jobs: {}".format(pprint.pformat(jobs))

    for processor in processors:
        print DELIMITER2
        print "Processor: {}".format(processor)
        lpt = LPT(jobs, processor)
        scheduled_jobs, loads = lpt.run()
        print "Scheduled Jobs: {}".format(pprint.pformat(scheduled_jobs))
        print "Loads: {}".format(pprint.pformat(loads))
        print DELIMITER2

    print DELIMITER1


def test_lpt_three():
    """Testing LPT algorithm with a large set of jobs with repititions."""
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
        lpt = LPT(jobs, processor)
        scheduled_jobs, loads = lpt.run()
        print "Scheduled Jobs: {}".format(pprint.pformat(scheduled_jobs))
        print "Loads: {}".format(pprint.pformat(loads))
        print DELIMITER2

    print DELIMITER1
