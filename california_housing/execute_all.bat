@echo off
if not exist "%~dp0Execution_Logs" ( mkdir "%~dp0Execution_Logs" )
REM setlocal enabledelayedexpansion
(
echo ==========================================================
echo Executing %~dp0src\data\1.0_make_dataset.py
python %~dp0src\data\1.0_make_dataset.py
echo Execution of %~dp0src\data\1.0_make_dataset.py completed
echo ==========================================================
echo Executing %~dp0notebooks\2.0_EDA.py
python %~dp0notebooks\2.0_EDA.py"
echo Execution of %~dp0notebooks\2.0_EDA.py completed
echo ==========================================================
echo Executing %~dp0src\data\3.0_split_data.py
python %~dp0src\data\3.0_split_data.py
echo Execution of %~dp0src\data\3.0_split_data.py completed
echo ==========================================================
echo Executing %~dp0notebooks\4.0_EDA.py
python %~dp0notebooks\4.0_EDA.py"
echo Execution of %~dp0notebooks\4.0_EDA.py completed
echo ==========================================================
echo Executing %~dp0src\data\5.0_Prepare_Data.py
python %~dp0src\data\5.0_Prepare_Data.py
echo Execution of %~dp0src\data\5.0_Prepare_Data completed
echo ==========================================================
echo Executing %~dp0src\models\6.0_train_modela.py
python %~dp0src\models\6.0_train_model.py
echo Execution of %~dp0src\models\6.0_train_model.py completed
echo ==========================================================
) > "%~dp0Execution_Logs\Execution_%DATE:~-4%%DATE:~-7,2%%DATE:~-10,2%_%time:~0,2%_%time:~3,2%_%time:~6,2%.log"

