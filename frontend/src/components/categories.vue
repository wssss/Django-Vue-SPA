<template>
  <div class="widget tag">
        <h3 class="title">
            Category
        </h3>
        <ul class="entry">
            <li v-for="category in categories">
                <a href="#">{{category.name}}</a><small>2</small>
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
                this.categories = res.data;
            })
        }
    }
}
</script>
</script>