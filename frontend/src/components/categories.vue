<template>
  <div class="widget tag">
        <h3 class="title">
            Category
        </h3>
        <ul class="entry">
            <li v-for="category in categories" :key="category.id">
                <router-link :to="{ name: 'posts', query: { 'category': category.id }}">
                    {{category.name}}
                </router-link><small>{{category.post_count}}</small>
            </li>
        </ul>
    </div>
</template>
<script>
export default{
    created(){
        this.getcategories();
    },
    data(){
        return {
            categories:[]
        }
    },
    methods:{
        getcategories(){
            this.$http.get('api/post/categories')
            .then(res => {
                this.categories = res.data.results;
            })
        }
    }
}
</script>
