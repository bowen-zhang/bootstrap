setup:
	sudo apt-get install -y default-jdk
	wget -O /tmp/zookeeper.tar.gz https://mirrors.koehn.com/apache/zookeeper/zookeeper-3.6.1/apache-zookeeper-3.6.1-bin.tar.gz
	sudo mkdir -p /opt/zookeeper
	sudo tar -C /opt/zookeeper --strip-components=1 -xvf /tmp/zookeeper.tar.gz
	sudo cp ./zoo.cfg ~/zookeeper/conf
	sudo cp ./zookeeper.service /etc/systemd/system/zookeeper.service
	sudo systemctl enable zookeeper
	sudo systemctl start zookeeper
