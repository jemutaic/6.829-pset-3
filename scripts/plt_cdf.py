import numpy as np
import json
import os
import sys
import argparse
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
sys.path.append('./')
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--runs', required=True, nargs='+', type=str)
parser.add_argument('--results_dir', type=str, default='results/')
args = parser.parse_args()

OUT_DIR = 'cdfs'


def plot_cdf(ax, vals, label='', download_rates=None):
  x = sorted(vals)
  y = [i / float(len(vals)) for i in range(len(vals))]
  # y = download_rates
  ax.plot(x, y, label=label + '(Avg: %.2f)' % np.mean(x))
  ax.legend()


def main():
  runs = sorted(args.runs)
  for mode in ['train', 'valid', 'test']:
    f, axarr = plt.subplots(2, 2)
    for run in runs:
      rebufs, smooths, qualities, qoes, download_rates = [], [], [], [], []
      d = os.path.join(args.results_dir, run, mode)
      for fname in os.listdir(d):
        with open(os.path.join(d, fname, 'results.json')) as f:
          j = json.load(f)
        rebufs.append(j['avg_rebuf_penalty'])
        smooths.append(j['avg_smoothness_penalty'])
        qualities.append(j['avg_quality_score'])
        qoes.append(j['avg_net_qoe'])
        download_rates.append(j['avg_download_rate'])

      plot_cdf(axarr[0][0], qualities, label=run, download_rates=download_rates)
      axarr[0][0].set_xlabel('quality score')
      plot_cdf(axarr[0][1], rebufs, label=run, download_rates=download_rates)
      axarr[0][1].set_xlabel('rebuf penalty')
      plot_cdf(axarr[1][0], smooths, label=run, download_rates=download_rates)
      axarr[1][0].set_xlabel('smooth penalty')
      plot_cdf(axarr[1][1], qoes, label=run, download_rates=download_rates)
      axarr[1][1].set_xlabel('net qoe')

    plt.tight_layout()
    utils.mkdir_if_not_exists(os.path.join(OUT_DIR, '_'.join(runs)))
    plt.savefig(os.path.join(OUT_DIR, '_'.join(runs), '%s.png' % mode))


if __name__ == '__main__':
  main()
