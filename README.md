# Music Trends Analysis (Spotify Audio Features)
Analyzing music trends based on Spotify audio features, song popularity, and recommendation system efficiency. Interactive Tableau dashboard can be found [here](https://wanjing4.github.io/Spotify-Analysis/).
## Overview
The goal of this project is to analyze music trends based on various audio features and assess the factors influencing song popularity.

## Research Questions
<a id="custom-details1"></a>
#### 1. Which songs have popularity >= 80, and who are their artists? What are the commonalities of their songs? [Go to conclusion](#popular-songs-analysis)
<a id="custom-details2"></a>
#### 2. Will key and mode affect the song's popularity?[Go to conclusion](#key-and-mode-analysis)
<a id="custom-details3"></a>
#### 3. Spotify sometimes recommends songs that have similar audio features. Does the weight on this recommendation algorithm perform well? [Go to conclusion](#spotify-recommendation-analysis)

## Key Metrics and Dimensions
- **Popularity**: The popularity score of each song (range: 0-100).
- **Audio Features**: Characteristics such as tempo, loudness, energy, and danceability.
- **Key and Mode**: Tonal properties that might influence popularity.
- **Recommendation Efficiency**: Evaluation of Spotify’s recommendation algorithm.


## Summary of Insights
### [Popular Songs Analysis](#custom-details1)
- Although number of pop music in a whole is lower than other genre, about 30% of high popular music is pop: ![5d501b7f76517a6a3346a89f27605a9](https://github.com/user-attachments/assets/2060300e-3e60-4419-9aee-775295bc621f)
![771a53b4677de78927bee97af215d01](https://github.com/user-attachments/assets/7758e6db-e442-4ca5-b1b2-8d31ad90b723)

- Some artists consistently produce high-popularity songs, contributing to trends in the industry.
- bullet point 3
- 
### [Key and Mode Analysis](#custom-details2)
- Statistical testing showed that certain keys and modes correlate with higher popularity, though not conclusively.
- bullet point2
- bullet point3
### [Spotify Recommendation Analysis](#custom-details3)
- The effectiveness of Spotify’s recommendation system was assessed, with suggestions for improving weighting of audio features.
- bullet point2
- bullet point

## Process

### Data Source
The Spotify data was downloaded from Kaggle[Spotify 1 Million Tracks Dataset](https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks)

### Data Description

The dataset collected includes about 1 Million tracks with 19 features between 2000 and 2023. Also, there is a total of 61,445 unique artists and 82 genres in the data.
The features includes:
- Popularity - Track popularity (0 to 100)
- Genre - Type of the music
- Aritist name - The name of person who made the music
- Year - Year released (2000 to 2023)
- Danceability - Track suitability for dancing (0.0 to 1.0)
- Energy - The perceptual measure of intensity and activity (0.0 to 1.0)
- Key - The key the track is in (0 to 11)
- Loudness - Overall loudness of track in decibels (-60 to 0 dB)
- Mode - Modality of the track (Major ‘1’ / Minor ‘0’)
- Speechiness - Presence of spoken words in the track
- Acousticness - Confidence measure from 0 to 1 of whether the track is acoustic
- Instrumentalness - Whether tracks contain vocals (0.0 to 1.0)
- Liveness - Presence of audience in the recording (0.0 – 1.0)
- Valence - Musical positiveness (0.0 to 1.0)
- Tempo - Tempo of the track in beats per minute (BPM)
- Time_signature - Estimated time signature (3 to 7)
- Duration_ms - Duration of track in milliseconds
- 
### Analysis Methods
- write functions here
- define input here

### Summary of Analysis output
- which category does the output belongs and what does it mean?
- bullet point2



## Recommendations & Next Steps
- Feature Selection Improvements: Refine feature selection methods to improve clustering and trend identification.
- Algorithm Adjustments: Suggest modifications to Spotify’s recommendation system based on findings.
- Data Visualization Enhancements: Enhance interactive Tableau dashboards to provide deeper insights into trends.

## Contact
Feel free to reach out:
- Email: wanjing@illinois.edu
- GitHub: wanjing4
