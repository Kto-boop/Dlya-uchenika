<template>
    <div v-if="currentTask == n">
        <div>
            {{ task.text }} <b>{{ task.expr }}</b><br>
            <table>
                <tr v-for="(row, i) in task.table" :key="i + '' + row">
                    <td v-for="(col, j) in row" :key="j + '' + col" :class="{ thead: i == 0 }">
                        {{ col }}
                    </td>
                </tr>
            </table>
            <span class="smaller">
                Значения логических операций есть на главной странице (в документации).<br>
                {{ task.hint || 'Других примечаний нет.'}}
            </span>
        </div>
        <div class="flex">
            <input type="text" v-model="answer" placeholder="Введите ответ" @keydown="$event.which == 13 && $emit('answer', answer)" ref="ans">
            <input type="button" value="Далее" @click="$emit('answer', answer)">
            <input type="button" :value="showAnswer ? 'Скрыть ответ' : 'Посмотреть ответ'" @click="showAnswer = !showAnswer" v-if="train">
        </div>
        <div v-if="showAnswer" style="margin-top: 8px">
            <div>Правильный ответ: {{ correctAnswer }}</div>
            <div v-if="hint">{{ hint }}</div>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    props: ['task', 'n', 'currentTask', 'train', 'hint', 'correctAnswer'],
    data: () => ({
        answer: '',
        showAnswer: false,
        prevTask: null
    }),
    updated() {
        this.$refs.ans.focus();
        if (this.prevTask != this.task) {
            this.resetState();
            this.prevTask = this.task;
            console.log(this.task);
        }
    },
    methods: {
        resetState() {
            this.showAnswer = false;
            this.answer = '';
        }
    }
}
</script>

<style scoped>
input {
    margin: 0pt;
    margin-left: 10px;
}
input[type="text"] {
    width: 80%;
}
input[type="button"] {
    flex-grow: 1;
}
.flex {
    display: flex;
    margin-top: 8pt;
}
div {
    text-align: left;
}
.smaller {
    font-size: 12px;
}
.bigger {
    font-size: 24px;
}
td {
    background: white;
}
.thead {
    background: rgba(255, 196, 0, 0.7);
}
</style>