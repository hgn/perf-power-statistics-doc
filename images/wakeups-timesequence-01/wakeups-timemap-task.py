#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

data = pd.read_csv("wakeups-timemap-task.txt", sep='\s+', header=0)
max_value = data.iloc[:, 3:].max().max()
data = data.head(30)
no_tasks = data.shape[0]

fig, axs = plt.subplots(no_tasks, 1, sharex=True, figsize=(30, 20))
for i, data in enumerate(data.iterrows()):
    index, row = data
    pid = row.iloc[0]
    tid = row.iloc[1]
    comm = row.iloc[2]
    row_mean_value = row.iloc[3:].mean()
    reshaped_array = np.array(row.iloc[3:].tolist()).reshape((1, -1))
    im = axs[i].imshow(reshaped_array, cmap=plt.cm.inferno_r, extent=[0, 10, 0, 10],
                       aspect='auto', interpolation='none', vmin=0, vmax=max_value)
    # I use TeX here for boldface font generatiom, remove textbf and usetex=False
    # to get rid of it
    text = f"\\textbf{{{comm}}} - Mean:{row_mean_value:.1f}\nPID: {pid}  TID: {tid}"
    axs[i].text(-1, 5, text, multialignment='left', va='center', ha='left', fontsize=12, usetex=True)

# add colorbar legend
cbar_ax = fig.add_axes([0.95, 0.1, 0.03, 0.8])
cbar = fig.colorbar(im, cax=cbar_ax)

# remove borders and make is look more modern
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)


plt.savefig('wakeups-timemap-task.pdf')
plt.savefig('wakeups-timemap-task.png')
