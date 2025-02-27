<template>
    <div>
        <b>1. What subject do you like?</b><br><br>
        <input type="text" v-model="answer.q1" placeholder="answer" maxlength="120"><br><br>

        <b>2. Which environment do you prefer working in?</b><br>
        <b>(such as WFH, customer service)</b><br><br>
        <input type="text" v-model="answer.q2" placeholder="answer" maxlength="120"><br><br>

        <b>3. What activities do you enjoy the most?</b><b>(hobbies)</b><br><br>
        <input type="text" v-model="answer.q3" placeholder="answer" maxlength="120"><br><br>

        <b>4.	What do people say about your personality? <br>And what do you think about it?</b><br><br>
        <input type="text" v-model="answer.q4" placeholder="answer" maxlength="120"><br><br>

        <b>5. What activities are you naturally good at?</b><br><br>
        <input type="text" v-model="answer.q5" placeholder="answer" maxlength="120"><br><br>

        <b>6. Do you prefer working alone or in a team?</b><br>
        <b>(in case you prefer working in a team,<br>
            do you enjoy leading projects, <br>or do you prefer supporting roles?)</b><br><br>
        <input type="text" v-model="answer.q6" placeholder="answer" maxlength="120"><br><br>

        <b>7.	Are you comfortable with continuous learning <br>
            and adapting to new trends?</b><br><br>
        <input type="text" v-model="answer.q7" placeholder="answer" maxlength="120"><br><br>
        <button v-on:click="getData">Submit</button>
    </div>
</template>
<script>
export default {
    name: 'Login',
    data(){
        return {
            answer:{
                q1:null,
                q2:null,
                q3:null,
                q4:null,
                q5:null,
                q6:null,
                q7:null
            }
        }
    },
    methods:{
        getData() 
        {
            console.log();
        }
    }
}


</script>


