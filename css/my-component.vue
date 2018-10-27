<!-- 
 Copyright 2018 Bowen Zhang

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http:www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.	
 -->

 <template>
<v-card>
	<v-card-title class="headline font-weight-regular blue-grey white--text">Profile</v-card-title>
	<v-card-text>
		<v-subheader class="pa-0">Where do you live?</v-subheader>
		<v-autocomplete
			:hint="'Start typing and see.'"
			:items="states"
			:label="'State'"
			persistent-hint
			prepend-icon="mdi-city"
		>
		</v-autocomplete>
	</v-card-text>
</v-card>
</template>

<script>
module.exports = {
	data: function() {
		return {
	        model: null,
	        states: [
	          'Alabama', 'Alaska', 'American Samoa', 'Arizona',
	          'Arkansas', 'California', 'Colorado', 'Connecticut',
	          'Delaware', 'District of Columbia', 'Federated States of Micronesia',
	          'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho',
	          'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
	          'Louisiana', 'Maine', 'Marshall Islands', 'Maryland',
	          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
	          'Missouri', 'Montana', 'Nebraska', 'Nevada',
	          'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
	          'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio',
	          'Oklahoma', 'Oregon', 'Palau', 'Pennsylvania', 'Puerto Rico',
	          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
	          'Texas', 'Utah', 'Vermont', 'Virgin Island', 'Virginia',
	          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
	        ]
		}
	}
};
</script>

<style scoped>
span {
	border: solid 1px red;
}
</style>