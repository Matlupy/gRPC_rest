import matplotlib.pyplot as plt



def plot_graph(performance_dict, service):
    
    volume = list(performance_dict.keys())
    time_taken = list(performance_dict.values())

    # plt.bar(range(len(performance_dict)), time_taken, tick_label=volume)
    # plt.show()

    plt.plot(volume, time_taken)
    plt.title('Performance of transactions using '+service+ ' service ')
    plt.xlabel('Volume')
    plt.ylabel('Time taken')
    plt.show()