# prepare environment
sudo apt install make python3-pip unzip
make install
sudo ln -s ~/.local/bin/kaggle /usr/bin/kaggle

# prepare java evnironment for pyspark
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# prepare data
KAGGLE_DATA=store-sales-time-series-forecasting
kaggle competitions download -c $KAGGLE_DATA
mkdir data
unzip $KAGGLE_DATA.zip -d data

#python3 happy_py.py