import matplotlib.pyplot as plt

def print_table(data):
    formatted_row = "{:<6}" * len(data)
    print(formatted_row.format(*data))
    
def plot_cop_over_temp(cop,temp):

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('days')
    ax1.set_ylabel('cop', color=color)
    ax1.plot(range(len(cop)), cop, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('temp', color=color)  # we already handled the x-label with ax1
    ax2.plot(range(len(temp)), temp, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()