setup:
	wget -O /tmp/kafka.tar.gz http://www.trieuvan.com/apache/kafka/2.5.0/kafka_2.12-2.5.0.tgz
	sudo mkdir -p /opt/kafka
	sudo tar -C /opt/kafka --strip-components=1 -xzf /tmp/kafka.tar.gz
	sudo sed -i 's/log.dirs=\/tmp\/kafka-logs/log.dirs=\/var\/kafka\/logs/g' /opt/kafka/config/server.properties
	sudo cp ./kafka.service /etc/systemd/system/kafka.service
	sudo systemctl enable kafka
	sudo systemctl start kafka