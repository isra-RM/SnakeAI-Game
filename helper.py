import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    
    plt.style.use('ggplot')  
    
    plt.title('Training Progress ...', fontsize=12, fontweight='bold')
    plt.xlabel('Number of Games', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    
    plt.plot(scores, label='Score', color='royalblue', linewidth=2)
    plt.plot(mean_scores, label='Mean Score', color='red', linestyle='--', linewidth=3)
    
    plt.ylim(ymin=0)
    
    plt.text(len(scores)-1, scores[-1], str(scores[-1]), color='royalblue')
    plt.text(len(mean_scores)-1, mean_scores[-1], str(round(mean_scores[-1],2)), color='red')
    
    plt.legend(loc='upper left', fontsize=12, framealpha=0.5)

    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    
    plt.tight_layout()  
    
    plt.show(block=False)
    plt.pause(.1)
