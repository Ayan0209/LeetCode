
        if(paths==null && paths.size() == 0){
            return "";
        }

        String start = paths.get(0).get(0);
        while(dest.containsKey(start)){
            start = dest.get(start);
        }

        return start;
        
[
