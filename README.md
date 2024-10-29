# 📊 Daily Temperature Analysis 🌡️

Welcome to the Daily Temperature Analysis repository. This project automates the generation, analysis, and visualization of daily temperature data using Python. The goal of this project is to showcase the integration of data analysis, visualization, and version control through Git.

## 🔍 Project Overview:
This project analyzes daily temperature data, generates plots, and stores the results.
The Python script get the weather data from [Open Meteo](https://open-meteo.com/) or as fallback it generates random temperature data for a day and plots it using the Matplotlib library. The temperature data is updated every 10 hours, and the resulting plot is automatically pushed to this repository. The project demonstrates how to schedule tasks using Windows Task Scheduler to automate data analysis and Git commits.

## 🚀 Features:
- Automated generation and visualization of realtime weather data or as fallback it generates random temperature data.
- Scheduled data analysis and Git push to update the repository.
- Utilizes Python's Pandas and Matplotlib libraries for data manipulation and visualization.
- A showcase of effective use of version control with Git and GitHub.

## 📋 Usage:
1. Clone this repository to your local machine.
2. Set up a Python virtual environment and install required dependencies.
   
   ```bash
   pip install -r requirements.txt
   ```

3. Schedule the `daily_temperature_analysis.py` script using Windows Task Scheduler.
4. Watch as the temperature plot is updated and automatically pushed to this repository.

## 📄 License:
This project is licensed under the [Apache 2.0 License](LICENSE).

## 🤝 Contributing:
Contributions are welcome! Feel free to open issues or pull requests for any improvements, bug fixes, or additional features.

## 👍 Credits:
### Data License
API data are offered under Attribution 4.0 International (CC BY 4.0)

You are free to share: copy and redistribute the material in any medium or format and adapt: remix, transform, and build upon the material.

Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

<a href="https://open-meteo.com/">Weather data by Open-Meteo.com</a>


### Source Code License
Open-Meteo is open-source under the GNU Affero General Public License Version 3 (AGPLv3) or any later version. You can [find the license here](https://github.com/open-meteo/open-meteo/blob/main/LICENSE). Exceptions are third party source-code with individual licensing in each file.

## 🔗 Links:
- [Author's GitHub Profile](https://github.com/pizofreude)
- [Task Scheduler Documentation](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)

Thank you for checking out the Daily Temperature Analysis project. Explore the code, learn, and adapt it for your data analysis projects.

