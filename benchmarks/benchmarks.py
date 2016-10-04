import os
import timeit

os.environ['OMP_NUM_THREADS'] = '1'  # ensure we are running single threaded


class TimeDemos:

    timer = timeit.default_timer  # use wall time for demos
    timeout = 60 * 60

    def teardown(self):
        from pymor.gui.qt import stop_gui_processes
        stop_gui_processes()

    def _run(self, module, args):
        import sys
        import runpy
        sys.argv = [module] + [str(a) for a in args]
        runpy.run_module(module, init_globals=None, run_name='__main__', alter_sys=True)

    def time_thermalblock_small(self):
        self._run('pymordemos.thermalblock', [2, 2, 2, 10])

    def time_thermalblock_highdim(self):
        self._run('pymordemos.thermalblock', [2, 2, 2, 10, '--grid=300'])

    def time_thermalblock_manymu(self):
        self._run('pymordemos.thermalblock', [2, 2, 16, 10, '--test=1'])

    def time_thermalblock_small_listva(self):
        self._run('pymordemos.thermalblock', [2, 2, 2, 10, '--list-vector-array'])

    def time_thermalblock_highdim_listva(self):
        self._run('pymordemos.thermalblock', [2, 2, 2, 10, '--grid=300', '--list-vector-array'])

    def time_thermalblock_manymu_listva(self):
        self._run('pymordemos.thermalblock', [2, 2, 16, 10, '--test=1', '--list-vector-array'])

    def time_burgersei_small(self):
        self._run('pymordemos.burgers_ei', [1, 2, 3, 40, 3, 10, '--test=0', '--cache-region=disk'])

    def time_burgersei_highdim(self):
        self._run('pymordemos.burgers_ei', [1, 2, 3, 40, 3, 10, '--test=0', '--cache-region=disk',
                                            '--grid=120', '--nt=200'])

    def time_burgersei_largecb(self):
        self._run('pymordemos.burgers_ei', [1, 2, 10, 700, 3, 10, '--test=0', '--cache-region=disk'])
