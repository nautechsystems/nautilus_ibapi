TWS_API_VERSION?=1019.01
TWS_API_FILENAME:="twsapi_macunix.${TWS_API_VERSION}.zip"


download_source:
	echo "Downloading source from ${TWS_API_FILENAME}"
	curl -O "https://interactivebrokers.github.io/downloads/${TWS_API_FILENAME}"

unzip_source:
	echo "Unzipping source"
	unzip -o "${TWS_API_FILENAME}"

replace_source:
	mv ./IBJts/source/pythonclient/* .

pre_clean:
	rm -rf ibapi
	rm -rf tests

clean:
	rm -rf ./IBJts
	rm -rf ./META-INF
	rm ${TWS_API_FILENAME} || true
	rm setup.py


update: pre_clean download_source unzip_source replace_source clean
