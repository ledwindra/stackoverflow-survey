import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statistics

class Dataset:
    
    def __init__(
        self,
        file_name='./data/survey_results_public.csv'
    ):
        self.file_name = file_name
    
    def load_data(
        self,
        is_indonesia=True
    ):
        df = pd.read_csv(self.file_name)
        if is_indonesia:
            return df[df['Country'] == 'Indonesia'].reset_index(drop=True)
        return df[df['Country'] != 'Indonesia'].reset_index(drop=True)

    def gender_dataframe(self, df):
        df = pd.DataFrame(df.groupby('Gender').size())
        df.columns = ['count']
        df['gender'] = df.index
        df = df.reset_index(drop=True)
        non_binary = pd.DataFrame([{
            'count': df[(df['gender'] != 'Man') & (df['gender'] != 'Woman')]['count'].sum(),
            'gender': 'Non-binary'
        }])
        df = pd.concat([df[(df['gender'] == 'Man') | (df['gender'] == 'Woman')], non_binary])
        df = df.reset_index(drop=True)
        df['pct'] = round(df['count'] / sum(df['count']), 4)

        return df

    def age_first_code(self, df):
        df = df[~df['Age1stCode'].isin(['Older than 85', 'Younger than 5 years'])]
        df = df[~df['Age1stCode'].isnull()]
        age = df['Age1stCode'].astype(int)
        age.name = 'age_first_code'

        return age
    
class Visualization(Dataset):
    XKCD = plt.xkcd()
    
    def __init__(
        self,
        font_name='Comic Sans MS',
        font_size=16,
    ):
        self.font = {
            'fontname': font_name,
            'size': font_size
        }
        self.legend_font = font_manager.FontProperties(
            family=font_name,
            weight='bold',
            style='normal',
            size=font_size
        )
        
    def visualize_gender(
        self,
        gender_world,
        gender_indonesia
    ):
        font = self.font
        legend_font = self.legend_font
        self.XKCD
        fig, ax = plt.subplots(figsize=(10, 5))
        bar_width = 0.35
        opacity = 0.9
        ax.bar(
            gender_world.index,
            height='pct',
            width=0.35,
            data=gender_world,
            alpha=opacity,
            color='black',
            label='World'
        )
        ax.bar(
            gender_indonesia.index + bar_width,
            height='pct',
            width=0.35,
            data=gender_indonesia,
            alpha=opacity,
            color='grey',
            label='Indonesia'
        )
        plt.title('Stackoverflow Developer Survey 2020', **font)
        plt.xticks(gender_world.index, **font)
        plt.yticks(**font)
        ax.legend(prop=legend_font)
        ax.set_xticklabels(('Man', 'Woman', 'Non-binary'))
        vals = ax.get_yticks()
        ax.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
        ax.legend()
        plt.show()
    
    def visualize_age(
        self,
        age_world,
        age_indonesia,
        label_world,
        label_indonesia,
        kde_color='black',
        median_color='red',
        xmax=80,
        suptitle='Persebaran usia pas pertama kali ngoding',
        caption='Garis merah: usia median'
    ):
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
        font = self.font
        sns.kdeplot(
            age_world,
            shade=True,
            color=kde_color,
            label=label_world,
            ax=ax[0]
        )
        sns.kdeplot(
            age_indonesia,
            shade=True,
            color=kde_color,
            label=label_indonesia,
            ax=ax[1]
        )
        ax[0].axvline(statistics.median(age_world), color=median_color)
        ax[1].axvline(statistics.median(age_indonesia), color=median_color)
        plt.xlim(0, xmax)
        fig.suptitle(suptitle, **font)
        fig.text(0.1, -0.01, caption, **font)
