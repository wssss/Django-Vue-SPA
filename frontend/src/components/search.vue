<template>
    <div class="search">
        <input type="text" name="search" v-model="searchText" @keyup.enter="onEnter" placeholder="search">
    </div>
</template>
<script>
export default {
    
    data(){
        return {
            searchText:''
        }
    },
    methods:{
        onEnter(){
            this.$router.push({name:'archives', query:{search: this.searchText}})
        }
    }
}
</script>

