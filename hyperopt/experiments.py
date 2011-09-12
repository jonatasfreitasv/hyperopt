"""
XXX
"""

__authors__   = "James Bergstra"
__copyright__ = "(c) 2010, Universite de Montreal"
__license__   = "3-clause BSD License"
__contact__   = "James Bergstra <pylearn-dev@googlegroups.com>"

import logging
import base

logger = logging.getLogger(__name__)

class SerialExperiment(base.Experiment):
    """
    """

    def run(self, N):
        bandit = self.bandit
        algo = self.bandit_algo

        for n in xrange(N):
            trial = algo.suggest(self.trials, self.Ys(), self.Ys_status(), 1)[0]
            result = bandit.evaluate(trial, base.Ctrl())
            logger.info('trial: %s' % str(trial))
            logger.info('result: %s' % str(result))
            self.trials.append(trial)
            self.results.append(result)